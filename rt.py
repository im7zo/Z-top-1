import datetime
import time
import os
import json
import platform
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.channels import CreateChannelRequest, GetFullChannelRequest
from telethon.errors import ChannelInvalidError, ChannelPrivateError
from config import client, start_time

# ملفات الإعدادات
CONFIG_FILE = "config.json"
GROUPS_FILE = "groups.json"
DATA_FOLDER = "data"
F7_FILE = os.path.join(DATA_FOLDER, "f7.json")

os.makedirs(DATA_FOLDER, exist_ok=True)

# تحميل وحفظ الإعدادات والمجموعات
def load_json_file(filename, default):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except Exception:
        return default

def save_json_file(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

config = load_json_file(CONFIG_FILE, {"store_private": True, "store_groups": True})
groups = load_json_file(GROUPS_FILE, {})
f7_data = load_json_file(F7_FILE, {})

# التأكد من صلاحية القناة
async def is_group_valid(chat_id):
    try:
        await client(GetFullChannelRequest(chat_id))
        return True
    except (ChannelInvalidError, ChannelPrivateError):
        return False

# إنشاء مجموعة التخزين إذا لم تكن موجودة أو غير صالحة
async def create_storage_group():
    if "storage_chat_id" not in groups or not await is_group_valid(groups["storage_chat_id"]):
        result = await client(CreateChannelRequest(
            title="مجمـوعـة التخـزيـن",
            about="لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامـة (وظيفتهـا تخزيـن رسـائل الخـاص.)",
            megagroup=True
        ))
        groups["storage_chat_id"] = result.chats[0].id
        save_json_file(GROUPS_FILE, groups)

# الأوامر

@client.on(events.NewMessage(pattern=r"^.تفعيل التخزين$"))
async def enable_storage(event):
    # تحقق من المالك - يمكنك إضافة تحقق هنا حسب الكود السابق
    config["store_private"] = True
    config["store_groups"] = True
    save_json_file(CONFIG_FILE, config)

    await create_storage_group()

    await client.send_message(groups["storage_chat_id"],
                              "✅ تم تفعيل التخزين من السورس\n• By : @cfc_5\n• 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙  𝐓𝐎𝐏 1")
    await event.edit("✅ تم تفعيل التخزين.")

@client.on(events.NewMessage(pattern=r"^.تعطيل التخزين$"))
async def disable_storage(event):
    # تحقق من المالك
    config["store_private"] = False
    config["store_groups"] = False
    save_json_file(CONFIG_FILE, config)
    await event.edit("❌ تم تعطيل التخزين.")

@client.on(events.NewMessage(incoming=True))
async def forward_private(event):
    if event.is_private and config.get("store_private", False):
        try:
            if "storage_chat_id" in groups:
                await client.forward_messages(groups["storage_chat_id"], event.message, event.sender_id)
        except Exception as e:
            print(f"⚠️ فشل تحويل رسالة الخاص: {e}")

@client.on(events.NewMessage(incoming=True))
async def forward_group_reply(event):
    if event.is_group and config.get("store_groups", False):
        if event.message.is_reply:
            try:
                replied = await event.get_reply_message()
                me = await client.get_me()
                if replied.from_id and replied.from_id.user_id == me.id:
                    chat = await event.get_chat()
                    sender = await event.get_sender()
                    msg_link = (f"https://t.me/c/{str(event.chat_id)[4:]}/{event.id}"
                                if str(event.chat_id).startswith("-100") else "لا يوجد رابط")
                    text = f"""#التــاكــات
⌔┊الكــروب: {chat.title}
⌔┊المـرسـل: {sender.first_name}
⌔┊الرابـط: {msg_link}
⌔┊الرسالة: {event.text or '[وسائط]'}
"""
                    if "storage_chat_id" in groups:
                        await client.send_message(groups["storage_chat_id"], text)
            except Exception as e:
                print(f"⚠️ فشل تحويل رسالة الكروب: {e}")


OWNER_FILE = "owner.json"

def get_owner_id():
    if os.path.exists(OWNER_FILE):
        with open(OWNER_FILE, "r") as f:
            return json.load(f).get("owner_id")
    return None

def set_owner_id(owner_id):
    with open(OWNER_FILE, "w") as f:
        json.dump({"owner_id": owner_id}, f)

@client.on(events.NewMessage(pattern=r"^.ا(?:يدي)?$"))
async def user_info(event):
    owner_id = get_owner_id()

    # تعيين المالك إذا لم يكن معينًا
    if owner_id is None:
        set_owner_id(event.sender_id)
        owner_id = event.sender_id
        print(f"✅ تم تعيين المالك تلقائيًا: {owner_id}")

    # تجاهل الطلبات من غير المالك
    if event.sender_id != owner_id:
        return

    try:
        await event.delete()
    except:
        pass


    # جلب معلومات المستخدم (إذا رد على أحد)
    replied_msg = await event.get_reply_message()
    if replied_msg:
        user = await replied_msg.get_sender()
        chat_id = replied_msg.chat_id
        reply_to_id = replied_msg.id
    else:
        user = await event.get_sender()
        chat_id = event.chat_id
        reply_to_id = None

    # جلب معلومات كاملة عن المستخدم
    full = await client(GetFullUserRequest(user.id))
    photos = await client(GetUserPhotosRequest(user.id, offset=0, max_id=0, limit=1))

    first_name = user.first_name or "لا يوجد"
    username = f"@{user.username}" if user.username else "لا يوجد"
    user_id = user.id
    rank = "مـالك الحساب" if user.is_self else "مستخدم"

    try:
        bio = getattr(full.full_user, 'about', None) or "لا يوجد"
    except:
        bio = "لا يوجد"

    photos_count = len(photos.photos)

    # عدّ عدد الرسائل في الشات الحالي
    try:
        msg_count = 0
        async for msg in client.iter_messages(chat_id, from_user=user.id):
            msg_count += 1
    except:
        msg_count = "؟"

    caption = f"""•⎚• مـعلومـات المسـتخـدم مـن بـوت 𝐙

ٴ⋆─┄─┄─┄─ 𝐙 ─┄─┄─┄─⋆
✦ الاســم  ⤎ {first_name}
✦ اليـوزر  ⤎ {username}
✦ الايـدي  ⤎ {user_id}
✦ الرتبــه  ⤎ {rank}
✦ الصـور  ⤎ {photos_count}
✦ الرسائل  ⤎ {msg_count}
✦ البايـو  ⤎ {bio}
ٴ⋆─┄─┄─┄─ 𝐙 ─┄─┄─┄─⋆"""

    # تحميل الصورة الشخصية إن وجدت
    profile_photo_path = None
    if photos_count > 0:
        try:
            profile_photo_path = await client.download_profile_photo(user.id, file=f"profile_{user.id}.jpg")
        except:
            profile_photo_path = None

    try:
        if profile_photo_path and os.path.exists(profile_photo_path):
            await client.send_file(chat_id, file=profile_photo_path, caption=caption, reply_to=reply_to_id)
            os.remove(profile_photo_path)
        else:
            await client.send_message(chat_id, caption, reply_to=reply_to_id)
    except Exception as e:
        print("فشل إرسال الكليشة:", e)

# ------------- أمر انتحال الحساب -------------
import os
import json
from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

# ملف المالك
OWNER_FILE = "owner.json"
original_info = {}

def get_owner_id():
    if os.path.exists(OWNER_FILE):
        with open(OWNER_FILE, "r") as f:
            return json.load(f).get("owner_id")
    return None

# --------- أمر انتحال حساب ---------
@client.on(events.NewMessage(pattern=r'^\.انتحال$'))
async def impersonate_user(event):
    global original_info

    OWNER_ID = get_owner_id()
    if OWNER_ID is None:
        await event.respond("⚠️ لم يتم تحديد المالك. تأكد من وجود ملف `owner.json` يحتوي `owner_id`.")
        return

    if event.sender_id != OWNER_ID:
        return

    user_msg = await event.get_reply_message()
    if not user_msg:
        await event.respond("❌ يجب الرد على رسالة الشخص الذي تريد انتحاله.")
        return

    sender = await user_msg.get_sender()

    # حفظ معلومات الحساب الأصلي
    me = await client.get_me()
    profile_photos = await client.get_profile_photos('me')
    original_info['first_name'] = me.first_name or ""
    original_info['last_name'] = me.last_name or ""

    try:
        full_me = await client(GetFullUserRequest(me.id))
        original_info['bio'] = getattr(full_me.full_user, 'about', '')[:70]
    except:
        original_info['bio'] = ""

    original_info['photo'] = None
    if profile_photos.total > 0:
        try:
            file = await client.download_media(profile_photos[0])
            original_info['photo'] = file
        except:
            pass

    # جلب معلومات الشخص المُراد انتحاله
    full_user = await client(GetFullUserRequest(sender.id))
    new_first = sender.first_name or ""
    new_last = sender.last_name or ""
    new_bio = getattr(full_user.full_user, 'about', '')[:70]

    await client(functions.account.UpdateProfileRequest(
        first_name=new_first,
        last_name=new_last,
        about=new_bio
    ))

    photos = await client.get_profile_photos(sender.id, limit=1)
    if photos:
        try:
            file = await client.download_media(photos[0])
            await client(functions.photos.UploadProfilePhotoRequest(
                file=await client.upload_file(file)
            ))
            os.remove(file)
        except:
            pass

    await event.respond("✅ تم انتحال الحساب بنجاح.")

# --------- أمر إعادة الشكل الأصلي ---------
@client.on(events.NewMessage(pattern=r'^\.اعادة$'))
async def restore_original(event):
    global original_info

    OWNER_ID = get_owner_id()
    if OWNER_ID is None:
        await event.respond("⚠️ لم يتم تحديد المالك. تأكد من وجود ملف `owner.json` يحتوي `owner_id`.")
        return

    if event.sender_id != OWNER_ID:
        return

    if not original_info:
        await event.respond("❌ لا توجد بيانات محفوظة لإعادتها.")
        return

    await client(functions.account.UpdateProfileRequest(
        first_name=original_info['first_name'],
        last_name=original_info['last_name'],
        about=original_info['bio']
    ))

    if original_info.get('photo'):
        try:
            await client(functions.photos.UploadProfilePhotoRequest(
                file=await client.upload_file(original_info['photo'])
            ))
            os.remove(original_info['photo'])
        except:
            pass

    original_info.clear()
    await event.respond("✅ تمت إعادة الحساب إلى شكله السابق.")

# ------------- أمر عد الرسائل -------------
@client.on(events.NewMessage(outgoing=True, pattern=r".رسائلي$"))
async def my_messages(event):
    global OWNER_ID
    if OWNER_ID is None:
        OWNER_ID = event.sender_id

    if event.sender_id != OWNER_ID:
        return

    count = 0
    async for message in client.iter_messages(event.chat_id, from_user='me'):
        count += 1
    await event.edit(f"📨 عدد رسائلك في هذه المحادثة: {count}")

@client.on(events.NewMessage(outgoing=True, pattern=r".رسائله$"))
async def his_messages(event):
    global OWNER_ID
    if OWNER_ID is None:
        OWNER_ID = event.sender_id

    if event.sender_id != OWNER_ID:
        return

    if event.is_group or event.is_channel:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            count = 0
            async for msg in client.iter_messages(event.chat_id, from_user=user_id):
                count += 1
            name = (await client.get_entity(user_id)).first_name
            await event.edit(f"📨 عدد رسائل {name} في هذه المجموعة: {count}")
        else:
            await event.edit("❗ يجب الرد على رسالة المستخدم.")
    else:
        await event.edit("❗ هذا الأمر يعمل فقط في المجموعات.")

# ------------- أمر فحص البوت -------------
import os
import json
import time
import datetime
import platform
from telethon import events

start_time = datetime.datetime.now()

# مسارات الملفات
FOLDER = "data"
os.makedirs(FOLDER, exist_ok=True)
FILE_PATH = os.path.join(FOLDER, "f7.json")
OWNER_FILE = os.path.join(FOLDER, "owner.json")

# تحميل بيانات الفحص
f7_data = {}
if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        f7_data = json.load(f)

def save_f7():
    with open(FILE_PATH, "w") as f:
        json.dump(f7_data, f)

# تعيين المالك تلقائياً إذا لم يكن محدداً
def get_owner_id():
    if os.path.exists(OWNER_FILE):
        with open(OWNER_FILE, "r") as f:
            return json.load(f).get("owner_id")
    else:
        return None

def set_owner_id(owner_id):
    with open(OWNER_FILE, "w") as f:
        json.dump({"owner_id": owner_id}, f)

# أمر الفحص
@client.on(events.NewMessage(pattern=r'^\.فحص$'))
async def ping(event):
    me = await client.get_me()

    if not get_owner_id():
        set_owner_id(me.id)

    if event.sender_id != get_owner_id():
        # لا تحذف رسالة غير المالك
        return

    try:
        await event.delete()
    except:
        pass


    if event.sender_id != get_owner_id():
        return

    start = time.perf_counter()
    temp = await event.respond("انتظر .")
    end = time.perf_counter()
    ping_time = round((end - start) * 1000)

    full_name = f"[{me.first_name}](tg://user?id={me.id})"
    pyver = platform.python_version()
    uptime = datetime.datetime.now() - start_time
    uptime_str = str(uptime).split('.')[0]

    await temp.delete()

    data = f7_data.get(str(me.id), {})
    message_template = data.get("text", (
        "┏━━━━━━━━━━━━━━━┓\n"
        "┃ ✦ 𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁 : `{pyver}`\n"
        "┃ ✦ 𝙸𝙳 : `{me.id}`\n"
        "┃ ✦ 𝚄𝙿𝚃𝙸𝙼𝙴 : `{uptime_str}`\n"
        "┃ ✦ 𝙽𝙰𝙼𝙴 : {full_name}\n"
        "┗━━━━━━━━━━━━━━━┛\n"
        "┏━━━━━━━━━━━━━━━┓\n"
        "┃ ✦ 𝙿𝙸𝙽𝙶 : `{ping_time}ms`\n"
        "┗━━━━━━━━━━━━━━━┛"
    ))

    try:
        message = message_template.format(
            ping_time=ping_time,
            pyver=pyver,
            uptime_str=uptime_str,
            me=me,
            full_name=full_name
        )
    except Exception as e:
        return await event.reply(f"❌ خطأ في الكليشة:\n{e}")

    image_path = data.get("image")

    if image_path and os.path.exists(image_path):
        await client.send_file(event.chat_id, image_path, caption=message, parse_mode='md')
    else:
        await event.respond(message, parse_mode='md')


# تعيين كليشة الفحص
@client.on(events.NewMessage(pattern=r'^\.تعيين كليشة الفحص$'))
async def set_f7_text(event):
    if event.sender_id != get_owner_id():
        return await event.reply("❌ هذا الأمر يخص المالك فقط.")

    user_id = str(event.sender_id)
    reply = await event.get_reply_message()
    if not reply or not reply.message:
        return await event.edit("❌ يجب الرد على رسالة تحتوي كليشة الفحص.")

    if user_id not in f7_data:
        f7_data[user_id] = {}

    f7_data[user_id]["text"] = reply.message
    save_f7()
    await event.edit("✅ تم حفظ كليشة الفحص.")


# تعيين صورة الفحص
@client.on(events.NewMessage(pattern=r'^\.تعيين صورة الفحص$'))
async def set_f7_image(event):
    if event.sender_id != get_owner_id():
        return await event.reply("❌ هذا الأمر يخص المالك فقط.")

    user_id = str(event.sender_id)
    reply = await event.get_reply_message()

    if not reply or not reply.photo:
        return await event.edit("❌ يجب الرد على صورة لتعيينها للفحص.")

    path = await reply.download_media(file=os.path.join(FOLDER, f"f7_{user_id}.jpg"))

    if user_id not in f7_data:
        f7_data[user_id] = {}

    f7_data[user_id]["image"] = path
    save_f7()
    await event.edit("✅ تم حفظ صورة الفحص.")


# حذف كليشة الفحص
@client.on(events.NewMessage(pattern=r'^\.حذف كليشة الفحص$'))
async def delete_f7_text(event):
    if event.sender_id != get_owner_id():
        return await event.reply("❌ هذا الأمر يخص المالك فقط.")

    user_id = str(event.sender_id)
    if user_id in f7_data and "text" in f7_data[user_id]:
        del f7_data[user_id]["text"]
        if not f7_data[user_id]:
            del f7_data[user_id]
        save_f7()
        await event.edit("✅ تم حذف كليشة الفحص.")
    else:
        await event.edit("❌ لا توجد كليشة فحص محفوظة.")


# حذف صورة الفحص
@client.on(events.NewMessage(pattern=r'^\.حذف صورة الفحص$'))
async def delete_f7_image(event):
    if event.sender_id != get_owner_id():
        return await event.reply("❌ هذا الأمر يخص المالك فقط.")

    user_id = str(event.sender_id)
    if user_id in f7_data and "image" in f7_data[user_id]:
        img = f7_data[user_id]["image"]
        if img and os.path.exists(img):
            os.remove(img)
        del f7_data[user_id]["image"]
        if not f7_data[user_id]:
            del f7_data[user_id]
        save_f7()
        await event.edit("✅ تم حذف صورة الفحص.")
    else:
        await event.edit("❌ لا توجد صورة فحص محفوظة.")