#Z
import os
import time
import platform
import datetime
import json
import re

from telethon import TelegramClient, events, functions
from telethon.tl.functions.channels import CreateChannelRequest, GetFullChannelRequest, JoinChannelRequest
from telethon.tl.functions.photos import GetUserPhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import GetHistoryRequest, DeleteHistoryRequest
from telethon.errors import ChannelInvalidError, ChannelPrivateError

api_id = 28427066
api_hash = "0e058d46282174dfbfd828a403d61ad6"
client = TelegramClient("session", api_id, api_hash)
import time
import asyncio
import aiohttp
from telethon import events
from telethon.tl.functions.messages import SetTypingRequest
from telethon.tl.types import SendMessageTypingAction, SendMessageRecordVideoAction, SendMessageRecordAudioAction
from telethon import events
from telethon import events
import random
from telethon import events
from telethon.tl.types import PeerUser
from telethon import events, functions
import asyncio
import asyncio
import datetime
import re
from telethon import events
import os
from telethon import events
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
import random
from telethon import events
from telethon.errors.rpcerrorlist import WebpageMediaEmptyError
from telethon import events
import random
from telethon import events
import asyncio
from telethon import events
from telethon import events
from telethon import events
from telethon import events
from telethon.tl.types import User
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserIsBlockedError, ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.contacts import BlockRequest, DeleteContactsRequest
from telethon import events
import json
from telethon import events
import os
import json
from telethon import events
import os
import json
from telethon import events
import random
from telethon import events
import random
from telethon import events

from telethon import events

@client.on(events.NewMessage(pattern=r"\.تجربة التحديث"))
async def commands_menu(event):
    await event.respond("✅ تم تجربة التحديث بنجاح!", link_preview=False)

from telethon import events
from telethon.tl.types import Channel, Chat, User, PeerUser
from telethon.tl.functions.photos import GetUserPhotosRequest

@client.on(events.NewMessage(pattern=r"^\.كشف الحساب$"))
async def delete_command(event):
    await event.delete()  # يحذف رسالة الأمر فقط

    me = await client.get_me()
    total_channels = 0
    total_groups = 0
    total_bots = 0
    total_chats = 0

    async for dialog in client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                total_groups += 1
            else:
                total_channels += 1
        elif isinstance(entity, Chat):
            total_groups += 1
        elif isinstance(entity, User):
            total_chats += 1
            if entity.bot:
                total_bots += 1

    # عدد صور الحساب فقط (وليس المحفوظات)
    photos = await client(GetUserPhotosRequest(
        user_id=me.id,
        offset=0,
        max_id=0,
        limit=100
    ))
    total_photos = len(photos.photos)

    msg = f"""•⎚• كشـف الحـساب مـن سورس 𝐙 
ٴ⋆─┄─┄─┄─ 𝐙 ─┄─┄─┄─⋆
✦ عدد القنوات: {total_channels}
✦ عدد الكروبات: {total_groups}
✦ عدد البوتات: {total_bots}
✦ عدد المحادثات: {total_chats}
✦ عدد صور الحساب: {total_photos}
ٴ⋆─┄─┄─┄─ 𝐙 ─┄─┄─┄─⋆
"""

    await event.respond(msg)

import json
import os
from telethon import events

SHORTCUTS_FILE = "shortcuts.json"
shortcuts_data = {}
shortcuts_enabled = True

# تحميل الاختصارات
if os.path.exists(SHORTCUTS_FILE):
    with open(SHORTCUTS_FILE, "r", encoding="utf-8") as f:
        shortcuts_data = json.load(f)

# حفظ الاختصارات
def save_shortcuts():
    with open(SHORTCUTS_FILE, "w", encoding="utf-8") as f:
        json.dump(shortcuts_data, f, ensure_ascii=False, indent=2)

# أمر: .اختصار + حرف (عند الرد على رسالة)
@client.on(events.NewMessage(pattern=r"^\.اختصار (.+)$"))
async def add_shortcut(event):
    if not event.is_edit:
        return await event.edit("⛔ يجب الرد على رسالة لإضافة اختصار.")
    
    key = event.pattern_match.group(1).strip()
    edit_msg = await event.get_edit_message()

    user_id = str(event.sender_id)
    if user_id not in shortcuts_data:
        shortcuts_data[user_id] = {}

    shortcuts_data[user_id][key] = edit_msg.raw_text
    save_shortcuts()
    await event.edit(f"✅ تم حفظ الاختصار `{key}` بنجاح.")

# أمر: .اختصاراتي
@client.on(events.NewMessage(pattern=r"^\.اختصاراتي$"))
async def list_shortcuts(event):
    user_id = str(event.sender_id)
    if user_id not in shortcuts_data or not shortcuts_data[user_id]:
        return await event.edit("🚫 لا تملك أي اختصارات حالياً.")
    
    text = "⎉╎قائمـة اختصـاراتـك:\n\n"
    for key in shortcuts_data[user_id]:
        text += f"⪼ `{key}`\n"
    await event.reply(text)

# أمر: .حذف اختصار + حرف
@client.on(events.NewMessage(pattern=r"^\.حذف اختصار (.+)$"))
async def delete_shortcut(event):
    key = event.pattern_match.group(1).strip()
    user_id = str(event.sender_id)

    if user_id in shortcuts_data and key in shortcuts_data[user_id]:
        del shortcuts_data[user_id][key]
        save_shortcuts()
        await event.edit(f"🗑️ تم حذف الاختصار `{key}` بنجاح.")
    else:
        await event.edit("🚫 لا يوجد اختصار بهذا الاسم.")

# أمر: .حذف اختصاراتي
@client.on(events.NewMessage(pattern=r"^\.حذف اختصاراتي$"))
async def delete_all_shortcuts(event):
    user_id = str(event.sender_id)
    if user_id in shortcuts_data:
        shortcuts_data[user_id] = {}
        save_shortcuts()
        await event.edit("🗑️ تم حذف جميع اختصاراتك.")
    else:
        await event.edit("🚫 لا تملك اختصارات.")

# أمر: تشغيل / ايقاف الاختصارات
shortcuts_enabled = True  # افتراضيًا مفعلة

@client.on(events.NewMessage(pattern=r"^\.?(تشغيل|ايقاف) الاختصارات$"))
async def toggle_shortcuts(event):
    global shortcuts_enabled
    cmd = event.pattern_match.group(1)

    if cmd == "تشغيل":
        shortcuts_enabled = True
        await event.reply("✅ تم تفعيل الاختصارات.")
    else:
        shortcuts_enabled = False
        await event.reply("🚫 تم إيقاف الاختصارات.")

# التحقق من الرسائل لاستخدام الاختصارات
@client.on(events.NewMessage())
async def handle_shortcuts(event):
    if not shortcuts_enabled or event.text is None:
        return

    user_id = str(event.sender_id)
    msg = event.raw_text.strip()

    if user_id in shortcuts_data and msg in shortcuts_data[user_id]:
        await event.edit(shortcuts_data[user_id][msg])

import os
import json
from telethon import events
from telethon.tl.types import DocumentAttributeAudio

# مجلد البصمات
FOLDER = "voice_commands"
os.makedirs(FOLDER, exist_ok=True)

# قاعدة البيانات
DB_FILE = "voice_commands.json"
OWNER_FILE = "owner.json"

# تحميل قاعدة البيانات
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        voice_db = json.load(f)
else:
    voice_db = {}

# تحميل أو تعيين المالك
if os.path.exists(OWNER_FILE):
    with open(OWNER_FILE, "r") as f:
        OWNER_ID = json.load(f).get("owner_id")
else:
    OWNER_ID = None

def save_owner(owner_id):
    with open(OWNER_FILE, "w") as f:
        json.dump({"owner_id": owner_id}, f)

def save_db():
    with open(DB_FILE, "w") as f:
        json.dump(voice_db, f, indent=2)

# ───── إضافة بصمه (للمالك فقط - بدون رسالة تعيين) ─────
@client.on(events.NewMessage(pattern=r'^/.اضف بصمه (.+)$'))
async def add_voice(event):
    global OWNER_ID

    if OWNER_ID is None:
        OWNER_ID = event.sender_id
        save_owner(OWNER_ID)

    if event.sender_id != OWNER_ID:
        return

    if not event.is_reply:
        return await event.reply("🔁 يجب الرد على **بصمة أو صوت**.")

    reply = await event.get_reply_message()
    if not reply.voice and not (
        reply.document and any(isinstance(attr, DocumentAttributeAudio) for attr in reply.document.attributes)
    ):
        return await event.reply("⚠️ هذه ليست بصمة ولا صوت!")

    cmd = event.pattern_match.group(1).strip().lower()
    file_path = os.path.join(FOLDER, f"{cmd}.ogg")

    await reply.download_media(file=file_path)
    voice_db[cmd] = file_path
    save_db()

    await event.delete()

# ───── حذف بصمه (للمالك فقط - يحذف الأمر) ─────
@client.on(events.NewMessage(pattern=r'^\.حذف بصمه (.+)$'))
async def delete_voice(event):
    if event.sender_id != OWNER_ID:
        return

    cmd = event.pattern_match.group(1).strip().lower()
    if cmd not in voice_db:
        return await event.reply("❌ لا يوجد بصمة بهذا الاسم.")

    try:
        os.remove(voice_db[cmd])
    except:
        pass

    del voice_db[cmd]
    save_db()

    await event.delete()

# ───── تشغيل بصمه (فقط للمالك - يحذف الأمر) ─────
@client.on(events.NewMessage(pattern=r'^\.([^\n]+)$'))
async def play_voice(event):
    if event.sender_id != OWNER_ID:
        return

    cmd = event.pattern_match.group(1).strip().lower()
    if cmd in voice_db:
        await client.send_file(event.chat_id, voice_db[cmd], reply_to=event.reply_to_msg_id)
        await event.delete()
# اسم ملف حفظ الكلمات المحظورة
BLOCK_FILE = "blocked_words.json"

# تحميل الكلمات المحظورة
def load_blocked():
    try:
        with open(BLOCK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

# حفظ الكلمات المحظورة
def save_blocked(data):
    with open(BLOCK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# أمر منع كلمة
@client.on(events.NewMessage(pattern=r"^\.منع كلمة (.+)"))
async def block_word(event):
    word = event.pattern_match.group(1).strip()
    chat_id = str(event.chat_id)

    blocked = load_blocked()
    if chat_id not in blocked:
        blocked[chat_id] = []

    if word in blocked[chat_id]:
        return await event.edit("❗ الكلمة ممنوعة مسبقًا.")
    
    blocked[chat_id].append(word)
    save_blocked(blocked)
    await event.edit(f"✅ تم منع الكلمة: `{word}`")

# أمر حذف كلمة من المنع
@client.on(events.NewMessage(pattern=r"^\.حذف كلمة المنع (.+)"))
async def unblock_word(event):
    word = event.pattern_match.group(1).strip()
    chat_id = str(event.chat_id)

    blocked = load_blocked()
    if chat_id in blocked and word in blocked[chat_id]:
        blocked[chat_id].remove(word)
        save_blocked(blocked)
        await event.edit(f"✅ تم حذف الكلمة من قائمة المنع: `{word}`")
    else:
        await event.edit("⚠️ هذه الكلمة غير موجودة في قائمة المنع.")

# أمر عرض قائمة الكلمات
@client.on(events.NewMessage(pattern=r"^\.قائمة الكلمات$"))
async def list_blocked_words(event):
    chat_id = str(event.chat_id)
    blocked = load_blocked()

    if chat_id not in blocked or not blocked[chat_id]:
        return await event.edit("📭 لا توجد كلمات ممنوعة في هذا الكروب.")

    words = "\n".join([f"• {word}" for word in blocked[chat_id]])
    await event.edit(f"⎉╎قائمة الكلمـات الممنوعـه هنـا هـي :\n\n{words}")

# مراقبة الرسائل وحذف الكلمات المحظورة
@client.on(events.NewMessage())
async def monitor_blocked_words(event):
    if not event.is_group:
        return

    chat_id = str(event.chat_id)
    blocked = load_blocked()

    if chat_id in blocked:
        for word in blocked[chat_id]:
            if word in event.raw_text:
                try:
                    await event.delete()
                    print(f"🗑️ تم حذف كلمة محظورة: {word}")
                except:
                    pass
                break
OWNER_ID = None  # يتحدد تلقائيًا أول مرة

# تحديد المالك تلقائيًا
async def is_owner(event):
    global OWNER_ID
    if OWNER_ID is None:
        OWNER_ID = event.sender_id
        print(f"✅ تم تحديد المالك تلقائيًا: {OWNER_ID}")
    return event.sender_id == OWNER_ID

@client.on(events.NewMessage(pattern=r'^\.تصفيه البوتات$'))
async def clean_and_block_bots(event):
    if not await is_owner(event):
        return  # تجاهل لغير المالك

    removed = 0
    blocked = 0

    async for dialog in client.iter_dialogs():
        user = dialog.entity
        if isinstance(user, User) and user.bot:
            try:
                # حذف المحادثة بالكامل
                await client.delete_dialog(user.id)
                removed += 1

                # حظر البوت حتى لا يتمكن من مراسلتك مجددًا
                await client(BlockRequest(user.id))
                blocked += 1
            except Exception as e:
                # ممكن تحط طباعة خطأ لو تريد
                continue

    await event.edit(f"🗑️ تم حذف {removed} بوت من المحادثات\n🚫 وتم حظر {blocked} بوت بنجاح.")
OWNER_ID = None  # يتحدد تلقائيًا عند أول استخدام

# تحديد المالك تلقائيًا
async def is_owner(event):
    global OWNER_ID
    if OWNER_ID is None:
        OWNER_ID = event.sender_id
        print(f"✅ تم تحديد المالك تلقائيًا: {OWNER_ID}")
    return event.sender_id == OWNER_ID

@client.on(events.NewMessage(pattern=r'^\.مغادرة القنوات$'))
async def leave_channels_but_admin(event):
    if not await is_owner(event):
        return  # تجاهل الأمر لغير المالك

    left = 0
    async for dialog in client.iter_dialogs():
        if dialog.is_channel and getattr(dialog.entity, 'broadcast', False):  # قناة فقط
            try:
                participant = await client(GetParticipantRequest(dialog.entity, 'me'))
                if not (getattr(participant.participant, 'admin_rights', None) or getattr(participant.participant, 'creator', False)):
                    await client(LeaveChannelRequest(dialog.entity))
                    left += 1
            except:
                continue
    await event.edit(f"📤 تم مغادرة القناة ← العدد: {left}")

@client.on(events.NewMessage(pattern=r'^\.مغادرة الكروبات$'))
async def leave_groups_but_admin(event):
    if not await is_owner(event):
        return  # تجاهل الأمر لغير المالك

    left = 0
    async for dialog in client.iter_dialogs():
        if dialog.is_channel and getattr(dialog.entity, 'megagroup', False):  # كروب فقط
            try:
                participant = await client(GetParticipantRequest(dialog.entity, 'me'))
                if not (getattr(participant.participant, 'admin_rights', None) or getattr(participant.participant, 'creator', False)):
                    await client(LeaveChannelRequest(dialog.entity))
                    left += 1
            except:
                continue
    await event.edit(f"📤 تم مغادرة الكروب ← العدد: {left}")

@client.on(events.NewMessage(pattern=r'^\.عداد$'))
async def start_timer(event):
    global counting_task

    if counting_task and not counting_task.done():
        await event.edit("⏱️ يوجد عداد شغال بالفعل.\nاكتب `.توقيف` لإيقافه.")
        return

    async def run_timer(message):
        minutes = 0
        seconds = 0
        sent = await message.edit("00:00")

        while True:
            await asyncio.sleep(1)
            seconds += 1
            if seconds == 60:
                seconds = 0
                minutes += 1

            time_str = f"{minutes:02}:{seconds:02}"
            try:
                await sent.edit(f"{time_str}")
            except Exception:
                break

            if minutes == 60:
                break

    counting_task = asyncio.create_task(run_timer(event))

@client.on(events.NewMessage(pattern=r'^\.توقيف$'))
async def stop_timer(event):
    global counting_task

    if counting_task and not counting_task.done():
        counting_task.cancel()
        await event.edit("✅ تم إيقاف العداد.")
    else:
        await event.edit("⚠️ لا يوجد عداد شغال حاليًا.")
@client.on(events.NewMessage(pattern=r'^\.مسح$'))
async def delete_reply_and_command(event):
    try:
        # حذف الرسالة اللي فيها الأمر .مسح
        await event.delete()
        
        # إذا كان رد على رسالة، نحذف الرسالة اللي انرد عليها
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            await reply_msg.delete()
    except Exception as e:
        print(f"خطأ أثناء الحذف: {e}")

ZM_channel = '@zzio5'  # ← قناة الشعر أو المقاطع الصوتية

# تخزين حالة التفعيل للمجموعات
poetry_enabled_groups = set()

# أمر .تفعيل الشعر
@client.on(events.NewMessage(pattern=r'^\.تفعيل الشعر$'))
async def enable_poetry(event):
    if event.is_group:
        poetry_enabled_groups.add(event.chat_id)
        await event.edit("✅ تم تفعيل ميزة إرسال الشعر عند كتابة 'شعر'.")
    else:
        await event.edit("❌ هذا الأمر يعمل فقط داخل المجموعات.")

# أمر .تعطيل الشعر
@client.on(events.NewMessage(pattern=r'^\.تعطيل الشعر$'))
async def disable_poetry(event):
    if event.is_group:
        poetry_enabled_groups.discard(event.chat_id)
        await event.edit("🚫 تم تعطيل ميزة إرسال الشعر في هذه المجموعة.")
    else:
        await event.edit("❌ هذا الأمر يعمل فقط داخل المجموعات.")

# أمر .شعر اليدوي
@client.on(events.NewMessage(pattern=r'^\.شعر$'))
async def ZM_audio(event):
    try:
        await event.delete()

        msg_id = random.randint(322, 357)
        msg = await client.get_messages(ZM_channel, ids=msg_id)

        if msg and msg.media and hasattr(msg.media, 'document'):
            attributes = msg.media.document.attributes
            is_voice = any(attr.__class__.__name__ == "DocumentAttributeAudio" and getattr(attr, 'voice', False) for attr in attributes)
            is_audio = any(attr.__class__.__name__ == "DocumentAttributeAudio" and not getattr(attr, 'voice', False) for attr in attributes)

            if is_voice or is_audio:
                await client.send_file(event.chat_id, msg)
                return

        await event.respond("↯ لم أجد شعر متاح.")
    except Exception as e:
        await event.respond(f"حدث خطأ: {e}")

# مراقبة كلمة "شعر" تلقائيًا
@client.on(events.NewMessage())
async def auto_poetry(event):
    if event.is_group and event.chat_id in poetry_enabled_groups:
        text = event.raw_text.lower()

        # تجاهل الأوامر
        if text.startswith("."):
            return

        if "شعر" in text:
            try:
                msg_id = random.randint(322, 357)
                msg = await client.get_messages(ZM_channel, ids=msg_id)

                if msg and msg.media and hasattr(msg.media, 'document'):
                    attributes = msg.media.document.attributes
                    is_voice = any(attr.__class__.__name__ == "DocumentAttributeAudio" and getattr(attr, 'voice', False) for attr in attributes)
                    is_audio = any(attr.__class__.__name__ == "DocumentAttributeAudio" and not getattr(attr, 'voice', False) for attr in attributes)

                    if is_voice or is_audio:
                        await client.send_file(event.chat_id, msg.audio, reply_to=event.id)
            except:
                pass  # تجاهل الأخطاء
import random
from telethon import events

Z_channel = '@zzio5'  # ضع هنا اسم قناتك مع @

@client.on(events.NewMessage(pattern=r'^\.قصيدة$'))
async def Z_audio(event):
    try:
        await event.delete()  # يحذف أمر .قصيدة
        msg_id = random.randint(121, 320)
        msg = await client.get_messages(Z_channel, ids=msg_id)

        if msg and (msg.audio or msg.voice):
            await client.send_file(event.chat_id, msg)
        else:
            await event.respond("↯ لم أجد قصيدة متاحة.")
    except Exception as e:
        await event.respond(f"حدث خطأ: {e}")


from telethon import events
import random

quran_channel = '@zzio5'  # ← قناة القرآن

# تخزين حالة التفعيل للمجموعات
quran_enabled_groups = set()

# تفعيل الميزة
@client.on(events.NewMessage(pattern=r'^\.تفعيل القران$'))
async def enable_quran(event):
    if event.is_group:
        quran_enabled_groups.add(event.chat_id)
        await event.edit("✅ تم تفعيل ميزة إرسال القرآن عند كتابة 'قران'.")
    else:
        await event.edit("❌ هذا الأمر يعمل فقط داخل المجموعات.")

# تعطيل الميزة
@client.on(events.NewMessage(pattern=r'^\.تعطيل القران$'))
async def disable_quran(event):
    if event.is_group:
        quran_enabled_groups.discard(event.chat_id)
        await event.edit("🚫 تم تعطيل ميزة إرسال القرآن في هذه المجموعة.")
    else:
        await event.edit("❌ هذا الأمر يعمل فقط داخل المجموعات.")

# أمر .قران لإرسال مقطع صوتي عشوائي

OWNER_ID = None  # سيتم تعيينه تلقائيًا بعد تشغيل السورس

@client.on(events.NewMessage(pattern=r'^\.قران$'))
async def quran_audio(event):
    global OWNER_ID
    if OWNER_ID is None:
        me = await client.get_me()
        OWNER_ID = me.id

    if event.sender_id != OWNER_ID:
        return  # تجاهل الأمر إذا مو من المالك

    try:
        await event.delete()
        msg_id = random.randint(8, 107)
        msg = await client.get_messages(quran_channel, ids=msg_id)

        if msg and msg.audio:
            await client.send_file(event.chat_id, msg)
        else:
            await event.respond("↯ لم أجد مقطع صوتي في الرسالة، حاول مرة أخرى.")
    except Exception as e:
        await event.respond(f"⚠️ حدث خطأ: {e}")

# المراقبة داخل المجموعات للكلمة "قران"
@client.on(events.NewMessage())
async def auto_quran(event):
    if event.is_group and event.chat_id in quran_enabled_groups:
        text = event.raw_text.lower()

        # تجاهل الأوامر التي تحتوي على "قران" مثل ".قران" أو ".تفعيل القران"
        if text.startswith("."):
            return

        if "قران" in text:
            try:
                msg_id = random.randint(8, 107)
                msg = await client.get_messages(quran_channel, ids=msg_id)

                if msg and msg.audio:
                    await client.send_file(event.chat_id, msg.audio, reply_to=event.id)
            except:
                pass  # تجاهل الأخطاء

from telethon import events

sad_channel = '@zzio5'  # غيّرها حسب اسم قناتك

# استخراج آيدي المالك عند أول استخدام
owner_id = None

async def check_owner(event):
    global owner_id
    if owner_id is None:
        me = await client.get_me()
        owner_id = me.id
    return event.sender_id == owner_id

# التحقق من نوع الرسالة
def is_audio(msg):
    return msg.voice or msg.audio if msg else False
@client.on(events.NewMessage(pattern=r'^\.اغمضتها$'))
async def handler4(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 358
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)
@client.on(events.NewMessage(pattern=r'^\.هزيمه مؤلمة$'))
async def sad_handler(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 116
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if msg and is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)

@client.on(events.NewMessage(pattern=r'^\.زيج حزين$'))
async def handler1(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 117
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)

@client.on(events.NewMessage(pattern=r'^\.ما يهمني$'))
async def handler2(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 115
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)

@client.on(events.NewMessage(pattern=r'^\.لعنه امون$'))
async def handler3(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 114
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)

@client.on(events.NewMessage(pattern=r'^\.ضحك 1$'))
async def handler4(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 113
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)

@client.on(events.NewMessage(pattern=r'^\.ضحك 2$'))
async def handler5(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 112
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)

@client.on(events.NewMessage(pattern=r'^\.خناجر$'))
async def handler6(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 111
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)

@client.on(events.NewMessage(pattern=r'^\.خابرني عاليوتيوب$'))
async def handler7(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 110
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)

@client.on(events.NewMessage(pattern=r'^\.ام لولي$'))
async def handler8(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 109
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)

@client.on(events.NewMessage(pattern=r'^\.اشك هدومي$'))
async def handler9(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 108
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)

@client.on(events.NewMessage(pattern=r'^\.زيج$'))
async def handler10(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 118
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)

@client.on(events.NewMessage(pattern=r'^\.اكل خرا$'))
async def handler11(event):
    if not await check_owner(event):
        return
    try:
        reply_to_msg_id = event.reply_to_msg_id or event.message.id
        await event.delete()
        msg_id = 119
        msg = await client.get_messages(sad_channel, ids=msg_id)
        if is_audio(msg):
            await client.send_file(event.chat_id, msg, reply_to=reply_to_msg_id)
        else:
            await client.send_message(event.chat_id, "↯ ما لقيت صوت بالرسالة.", reply_to=reply_to_msg_id)
    except Exception as e:
        await client.send_message(event.chat_id, f"✗ خطأ: {e}", reply_to=reply_to_msg_id)
# تعريف المتغيرات قبل الاستخدام
time_task_name = None
original_name = ""
time_task_bio = None
original_bio = ""
# قائمة الأسئلة العشوائية
questions_list = [
    "حكي ودك يوصل للشخص المطلوب ؟",
    "منشن شخص تسولف معه تنسى هموم الدنيا ؟",
    "مقوله او مثل او بيت شعر قريب من قلبك؟",
    "اكثر مكان تحب تروح له ف الويكند ؟",
    "كم وجبه تآكل ف اليوم ؟",
    "كم ساعه تنام ف اليوم ؟",
    "هل وثقت ف احد و خذلك ؟",
    "كلمه تعبر عن شعورك ؟",
    "منشن شخص فاهمك ف كل شيء ؟",
    "اصدقاء المواقع افضل من الواقع تتفق؟",
    "كلمه معينه م يفهمها الا اصحابك ؟",
    "كل شيء يهون الا ؟",
    "كيف تتصرف مع شخص تكلمه في سالفه مهمه ويصرفك ومعد يرد ابداً؟",
    "ثلاث اشياء جنبك الحين ؟",
    "تشوف انو التواصل بشكل يومي من اساسيات الحب ؟",
    "نوعيات ودك ينقرضون من تويتر؟",
    "ماذا تفعل عندما تري دموع زوجتك؟",
    "ما هي هوايتك المفضلة؟",
    "لو خيروك تسافر لأي مكان في العالم، وين بتروح؟",
    "ايش اكثر اكلة تحبها؟",
    "ايش اكثر لون تحبه؟",
    "تحب القهوة او الشاي؟",
    "ايش موقف صار لك ما تنساه؟",
    "ايش اكثر شيء يضايقك؟",
    "ايش اكثر شيء يسعدك؟",
    "ايش هي امنيتك في الحياة؟",
    "لو كان بإمكانك تغيير شيء واحد في العالم، ماذا سيكون؟",
    "هل تؤمن بالحب من اول نظرة؟",
    "هل انت شخص صباحي او مسائي؟",
    "ما هو برجك؟",
    "ما هو فيلمك المفضل؟",
    "ما هي اغنيتك المفضلة؟",
    "ما هي فرقتك الموسيقية المفضلة؟",
    "ما هو كتابك المفضل؟",
    "ما هو مسلسل Netflix المفضل لديك؟",
    "هل تفضل الصيف او الشتاء؟",
    "هل تفضل العيش في المدينة او الريف؟",
    "هل تفضل الكلاب او القطط؟",
    "ما هو رأيك في وسائل التواصل الاجتماعي؟",
    "ما هي نصيحتك لأي شخص يمر بيوم سيء؟",
    "ما هو الشيء الذي تفتخر به؟",
    "ما هو الشيء الذي تخاف منه؟",
    "ما هو الشيء الذي يجعلك تضحك؟",
    "ما هو الشيء الذي يجعلك تبكي؟",
    "ما هو الشيء الذي يجعلك تشعر بالامتنان؟",
    "ما هو تعريفك للسعادة؟",
    "ما هو تعريفك للنجاح؟",
    "لو كان بإمكانك امتلاك اي قوة خارقة، ماذا ستختار؟",
    "لو كان بإمكانك العودة بالزمن، الى اي فترة زمنية ستعود؟",
    "من هو مثلك الأعلى؟",
    "ما هي أكبر غلطة سويتها في حياتك؟",
    "ما هو الدرس اللي تعلمته من هذي الغلطة؟",
    "ما هي أفضل نصيحة  انعطت لك؟",
    "ايش اكثر شيء تعلمته من والديك؟",
    "ايش اكثر شيء تحبه في نفسك؟",
    "ايش اكثر شيء تكرهه في نفسك؟",
    "كيف تصف نفسك في ثلاث كلمات؟",
    "ما هو الشيء الذي يميزك عن غيرك؟",
    "ما هي طموحاتك المستقبلية؟",
    "ما هو الشيء الذي تتمنى تحقيقه قبل ما تموت؟",
    "هل تؤمن بالحياة بعد الموت؟",
    "هل تؤمن بالأشباح؟",
    "هل تؤمن بالكائنات الفضائية؟",
    "ما هو رأيك في الذكاء الاصطناعي؟",
    "هل تعتقد أن الروبوتات ستسيطر على العالم؟",
    "ما هو الشيء الذي يجعلك تشعر بالغضب؟",
    "ما هو الشيء الذي يجعلك تشعر بالخجل؟",
    "ما هو الشيء الذي يجعلك تشعر بالذنب؟",
    "ما هو الشيء الذي يجعلك تشعر بالخوف؟",
    "ما هو الشيء الذي يجعلك تشعر بالحزن؟",
    "ما هو الشيء الذي يجعلك تشعر بالوحدة؟",
    "ما هو الشيء الذي يجعلك تشعر بالقلق؟",
    "ما هو الشيء الذي يجعلك تشعر بالإحباط؟",
    "ما هو الشيء الذي يجعلك تشعر بالملل؟",
    "ما هو الشيء الذي يجعلك تشعر بالتعب؟",
    "ما هو الشيء الذي يجعلك تشعر بالجوع؟",
    "ما هو الشيء الذي يجعلك تشعر بالعطش؟",
    "ما هو الشيء الذي يجعلك تشعر بالنعاس؟",
    "ما هو الشيء الذي يجعلك تشعر بالبرد؟",
    "ما هو الشيء الذي يجعلك تشعر بالحر؟",
    "ما هو الشيء الذي يجعلك تشعر بالألم؟",
    "ما هو الشيء الذي يجعلك تشعر بالراحة؟",
    "ما هو الشيء الذي يجعلك تشعر بالحب؟",
    "ما هو الشيء الذي يجعلك تشعر بالكراهية؟",
    "ما هو الشيء الذي يجعلك تشعر بالغيرة؟",
    "ما هو الشيء الذي يجعلك تشعر بالحسد؟",
    "ما هو الشيء الذي يجعلك تشعر بالندم؟",
    "ما هو الشيء الذي يجعلك تشعر بالذل؟",
    "ما هو الشيء الذي يجعلك تشعر بالمهانة؟",
    "ما هو الشيء الذي يجعلك تشعر بالظلم؟",
    "ما هو الشيء الذي يجعلك تشعر بالغفران؟",
    "ما هو الشيء الذي يجعلك تشعر بالشكر؟",
    "ما هو الشيء الذي يجعلك تشعر بالاحترام؟",
    "ما هو الشيء الذي يجعلك تشعر بالتقدير؟",
    "ما هو الشيء الذي يجعلك تشعر بالثقة؟",
    "ما هو الشيء الذي يجعلك تشعر بالأمان؟",
    "ما هو الشيء الذي يجعلك تشعر بالسعادة؟"
]

# روابط الصور من قناة تليجرام
image_links = [f"https://t.me/CNN9N/{i}" for i in range(10, 143)]

# أوامر: .كت | .انمي
@client.on(events.NewMessage(outgoing=True, pattern=r"^\.كت$|^\.انمي$"))
async def send_question_or_anime(event):
    await event.delete()
    chat = await event.get_chat()
    cmd = event.raw_text.strip()

    if cmd == ".كت":
        question = random.choice(questions_list)
        await client.send_message(chat, question)

    elif cmd == ".انمي":
        for _ in range(5):  # يحاول حتى 5 مرات في حال حدوث خطأ
            try:
                link = random.choice(image_links)
                channel, msg_id = link.split("/")[-2:]
                message = await client.get_messages(channel, ids=int(msg_id))
                await client.send_message(chat, "من عمك بنيامين:", file=message, silent=True)
                break
            except WebpageMediaEmptyError:
                continue
# مسار ملف الحفظ
channel_file = "forced_channel.txt"

# أمر: .اضافة قناة
@client.on(events.NewMessage(pattern=r'^\.اضافة قناة(?: (.+))?$'))
async def add_forced_channel(event):
    input_channel = event.pattern_match.group(1)
    if not input_channel:
        return await event.reply("📌 استخدم الأمر هكذا:\n`.اضافة قناة @YourChannel`")
    
    # حفظ القناة في ملف
    with open(channel_file, "w") as f:
        f.write(input_channel.strip().replace("@", ""))
    await event.reply(f" تم تفعيل الاشتراك الإجباري على قناة:\n@{input_channel.strip().replace('@','')}")

# أمر: .حذف قناة
@client.on(events.NewMessage(pattern=r'^\.حذف قناة$'))
async def remove_forced_channel(event):
    if os.path.exists(channel_file):
        os.remove(channel_file)
        await event.reply(" تم حذف الاشتراك الإجباري.")
    else:
        await event.reply(" لا يوجد اشتراك إجباري مفعل حالياً.")

# التحقق من الاشتراك عند أي رسالة في الخاص
@client.on(events.NewMessage(incoming=True))
async def check_private(event):
    if not event.is_private:
        return

    sender = await event.get_sender()
    if sender.bot:
        return

    if not os.path.exists(channel_file):
        return  # لا يوجد اشتراك إجباري

    # قراءة اسم القناة
    with open(channel_file, "r") as f:
        channel_username = f.read().strip()

    try:
        await client(GetParticipantRequest(channel=channel_username, participant=event.sender_id))
    except UserNotParticipantError:
        await event.reply(f"""🚫 لا يمكنك مراسلتي.

اشترك بالقناة ثم ارجع ارسل رسالتك
 https://t.me/{channel_username}

""")
        try:
            await event.delete()
        except:
            pass
@client.on(events.NewMessage(pattern=r'^\.حذف رسائلي(?: (\d+))?$'))
async def delete_my_messages(event):
    if not event.is_group:
        return await event.reply("❗ هذا الأمر يعمل فقط داخل المجموعات.")

    count = event.pattern_match.group(1)
    user_id = event.sender_id
    deleted = 0

    await event.edit("جاري الحذف")

    async for msg in event.client.iter_messages(event.chat_id, from_user=user_id):
        if count and deleted >= int(count):
            break
        try:
            await msg.delete()
            deleted += 1
        except:
            pass  # تجاهل أي خطأ (مثل الرسائل القديمة أو المحمية)

    await event.respond(f" تم حذف {deleted} من رسائلك.")
final = False

async def final_nshr(client, sleeptimet, chat, message, seconds):
    global final
    final = True
    while final:
        if message.media:
            await client.send_file(chat, message.media, caption=message.text)
        else:
            await client.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+) (@?\S+)$"))
async def final_handler(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("   يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا   ")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    global final
    final = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await client.get_entity(chat_username)
            await final_nshr(client, seconds, chat.id, message, seconds)
        except Exception as e:
            await event.reply(f"   لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}")
        await asyncio.sleep(1)

async def final_allnshr(client, sleeptimet, message):
    global final
    final = True
    final_chats = await client.get_dialogs()
    while final:
        for chat in final_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await client.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await client.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر_كروبات (\d+)$"))
async def final_handler(event):
    await event.delete()
    try:
        sleeptimet = int(event.pattern_match.group(1))
    except Exception:
        return await event.reply("   يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا   ")
    message = await event.get_reply_message()
    global final
    final = True
    await final_allnshr(client, sleeptimet, message)

super_groups = ["super", "سوبر"]

async def final_supernshr(client, sleeptimet, message):
    global final
    final = True
    final_chats = await client.get_dialogs()
    while final:
        for chat in final_chats:
            if chat.is_group and any(keyword in chat.title.lower() for keyword in super_groups):
                try:
                    if message.media:
                        await client.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await client.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def final_handler(event):
    await event.delete()
    try:
        sleeptimet = int(event.pattern_match.group(1))
    except Exception:
        return await event.reply("   يجب استخدام كتابة صحيحة الرجاء التاكد من الامر   اولا")
    message = await event.get_reply_message()
    global final
    final = True
    await final_supernshr(client, sleeptimet, message)

@client.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_final(event):
    global final
    final = False
    await event.edit("**  ︙ تم ايقاف النشر التلقائي بنجاح ✓  ** ")

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.وسبام$"))
async def word_spam_handler(event):
    await event.delete()
    message = await event.get_reply_message()
    if not message or not message.text:
        return await event.reply("   يجب الرد على رسالة نصية لاستخدام هذا الأمر.")
    words = message.text.split()
    for word in words:
        await event.respond(word)
        await asyncio.sleep(1)

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.تناوب (\d+)$"))
async def rotate_handler(event):
    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("   يجب الرد على رسالة لاستخدام هذا الأمر.")
    global final
    final = True
    chats = await client.get_dialogs()
    groups = [chat for chat in chats if chat.is_group]
    num_groups = len(groups)
    current_group_index = 0
    while final:
        try:
            if message.media:
                await client.send_file(groups[current_group_index].id, message.media, caption=message.text)
            else:
                await client.send_message(groups[current_group_index].id, message.text)
        except Exception as e:
            print(f"Error in sending message to chat {groups[current_group_index].id}: {e}")
        current_group_index = (current_group_index + 1) % num_groups
        await asyncio.sleep(seconds)

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.خاص$"))
async def private_handler(event):
    await event.delete()
    message = await event.get_reply_message()
    if not message:
        return await event.reply("   يجب الرد على رسالة لاستخدام هذا الأمر.")
    chats = await client.get_dialogs()
    private_chats = [chat for chat in chats if chat.is_user]
    for chat in private_chats:
        try:
            if message.media:
                await client.send_file(chat.id, message.media, caption=message.text)
            else:
                await client.send_message(chat.id, message.text)
        except Exception as e:
            print(f"Error in sending message to chat {chat.id}: {e}")

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.نقط (\d+)$"))
async def dot_handler(event):
    await event.delete()
    seconds = int(event.pattern_match.group(1))
    reply_to_msg = await event.get_reply_message()
    if not reply_to_msg:
        return await event.reply("   يجب الرد على رسالة لاستخدام هذا الأمر.")
    global final
    final = True
    while final:
        await reply_to_msg.reply(".")
        await asyncio.sleep(seconds)

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.مكرر (\d+)$"))
async def repeat_handler(event):
    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("   يجب الرد على رسالة لاستخدام هذا الأمر.")
    global final
    final = True
    while final:
        await message.respond(message)
        await asyncio.sleep(seconds)
# الاسم الوقتي بتنسيق 12 ساعة بدون AM/PM
@client.on(events.NewMessage(pattern=r'^\.اسم وقتي$'))
async def start_name_time(event):
    global time_task_name, original_name

    me = await client.get_me()
    original_name = me.first_name

    if time_task_name:
        await event.edit("⏱️ الاسم الوقتي مضاف مسبقًا.")
        return

    async def update_name():
        while True:
            now = datetime.datetime.now().strftime("%I:%M").lstrip("0")  # إزالة الصفر من البداية إن وجد
            new_name = f"{original_name} | {now}"
            try:
                await client(functions.account.UpdateProfileRequest(first_name=new_name))
            except:
                pass
            await asyncio.sleep(60)

    time_task_name = asyncio.create_task(update_name())
    await event.edit("✅ تم تفعيل الاسم الوقتي بنجاح.")

@client.on(events.NewMessage(pattern=r'^\.ايقاف الاسم$'))
async def stop_name_time(event):
    global time_task_name, original_name

    if time_task_name:
        time_task_name.cancel()
        time_task_name = None
        if original_name:
            try:
                await client(functions.account.UpdateProfileRequest(first_name=original_name))
            except:
                pass
        await event.edit("🕓 تم إيقاف الاسم الوقتي بنجاح.")
    else:
        await event.edit("⚠️ لا يوجد اسم وقتي مفعّل حالياً.")


# البايو الوقتي بتنسيق 12 ساعة بدون AM/PM
@client.on(events.NewMessage(pattern=r'^\.بايو وقتي$'))
async def start_bio_time(event):
    global time_task_bio, original_bio

    me = await client(functions.users.GetFullUserRequest(id='me'))
    original_bio = me.full_user.about or ""

    if time_task_bio:
        await event.edit("📄 البايو الوقتي مضاف مسبقًا.")
        return

    async def update_bio():
        while True:
            now = datetime.datetime.now().strftime("%I:%M").lstrip("0")  # إزالة الصفر من البداية
            new_bio = f"{original_bio} | {now}"
            try:
                await client(functions.account.UpdateProfileRequest(about=new_bio))
            except:
                pass
            await asyncio.sleep(60)

    time_task_bio = asyncio.create_task(update_bio())
    await event.edit("✅ تم تفعيل البايو الوقتي بنجاح.")

@client.on(events.NewMessage(pattern=r'^\.ايقاف البايو$'))
async def stop_bio_time(event):
    global time_task_bio, original_bio

    if time_task_bio:
        time_task_bio.cancel()
        time_task_bio = None
        if original_bio is not None:
            try:
                await client(functions.account.UpdateProfileRequest(about=original_bio))
            except:
                pass
        await event.edit("📴 تم إيقاف البايو الوقتي بنجاح.")
    else:
        await event.edit("⚠️ لا يوجد بايو وقتي مفعّل حالياً.")
# قائمة لتخزين المستخدمين المقلدين
trad_users = set()

@client.on(events.NewMessage(pattern=r"\.تقليد"))
async def start_mimic(event):
    if not event.is_reply:
        await event.edit("↯︙يجب الرد على رسالة الشخص الذي تريد تقليده.")
        return
    replied = await event.get_reply_message()
    user_id = replied.sender_id
    trad_users.add(user_id)
    await event.edit(f"⎙ بدأ تقليد هذا المستخدم [ID: {user_id}]")

@client.on(events.NewMessage(pattern=r"\.ايقاف التقليد"))
async def stop_mimic(event):
    if not event.is_reply:
        await event.edit("↯︙يجب الرد على رسالة الشخص لإيقاف تقليده.")
        return
    replied = await event.get_reply_message()
    user_id = replied.sender_id
    trad_users.discard(user_id)
    await event.edit(f"⎙ تم إيقاف تقليد هذا المستخدم [ID: {user_id}]")

@client.on(events.NewMessage())
async def mimic_messages(event):
    if event.sender_id in trad_users and not event.out:
        try:
            await client.send_message(event.chat_id, event.raw_text)
        except Exception as e:
            print(f"حدث خطأ أثناء تقليد الرسالة: {e}")
@client.on(events.NewMessage(pattern=r"\.زواج"))
async def zawaj(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        user = await replied.get_sender()
        name = f"[{user.first_name}](tg://user?id={user.id})"
        await event.edit(f"💍 تم زواجك من {name} 👰‍♂️\nمنك المال ومنها العيال")
    else:
        await event.edit("↯︙يجب الرد على رسالة الشخص الذي تريد الزواج منه.")

@client.on(events.NewMessage(pattern=r"\.طلاك"))
async def talaq(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        user = await replied.get_sender()
        name = f"[{user.first_name}](tg://user?id={user.id})"
        await event.edit(f"💔 تم طلاقك من {name}.\nنتمنى لك حياة أفضل")
    else:
        await event.edit("↯︙يجب الرد على رسالة الشخص الذي تريد تطليقه.")

@client.on(events.NewMessage(pattern=r"\.نسبة (.+)"))
async def nesba(event):
    text = event.pattern_match.group(1)
    percent = random.randint(0, 100)
    await event.edit(f" نسبة {text} هي {percent}%")

@client.on(events.NewMessage(pattern=r"\.نسبتنا (.+)"))
async def nesbatna(event):
    text = event.pattern_match.group(1)
    percent = random.randint(0, 100)
    await event.edit(f" نسبتنا في {text} هي {percent}%")

@client.on(events.NewMessage(pattern=r"\.بوسة"))
async def bosa(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        user = await replied.get_sender()
        name = f"[{user.first_name}](tg://user?id={user.id})"
        await event.edit(f"💋 أرسل بوسة إلى {name}")
    else:
        await event.edit("↯︙يجب الرد على رسالة الشخص الذي تريد تبوسه.")
@client.on(events.NewMessage(pattern=r'^\.اكس او$'))
async def start_xo(event):
    try:
        await event.delete()  # حذف رسالة الأمر

        result = await client.inline_query("xoBot", "play")
        if result:
            await result[0].click(event.chat_id)
        else:
            await event.respond("ما قدرنا نحصل على نتائج من @xoBot.")
    except Exception as e:
        await event.respond(f"حدث خطأ: {str(e)}")
from telethon import events
import re

@client.on(events.NewMessage(pattern=r"\.مقيد(?:\s+)?(https?://t\.me/[^\s]+)?"))
async def restricted_forward(event):
    match = event.pattern_match.group(1)

    if not match:
        await event.edit("❌ الرجاء إرسال الرابط بعد الأمر مباشرة.")
        return

    try:
        await event.edit("🔁 جارٍ جلب الرسالة...")
        # استخراج بيانات الرابط
        link = match
        parsed = re.search(r"(https?://t\.me/)(?P<username>[^/]+)/(?P<message_id>\d+)", link)
        if not parsed:
            await event.edit("❌ رابط غير صالح.")
            return

        username = parsed.group("username")
        msg_id = int(parsed.group("message_id"))

        # جلب الرسالة
        msg = await client.get_messages(username, ids=msg_id)

        if not msg:
            await event.edit("❌ لم يتم العثور على الرسالة.")
            return

        # إرسالها للرسائل المحفوظة
        await client.send_message("me", msg)

        await event.edit("✅ تم حفظ الرسالة في الرسائل المحفوظة.")
    except Exception as e:
        await event.edit(f"❌ فشل في جلب الرسالة.\nالخطأ: {e}")
from telethon import events
import asyncio
import random
import string
import time

@client.on(events.NewMessage(pattern=r'\.ايميل وهمي'))
async def fake_email(event):
    try:
        user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = user + '@gmail.com'
        await event.edit(f"📩 تم إنشاء بريد وهمي:\n`{email}`\n(من عمكم بنيامين)")
    except Exception as e:
        await event.edit("❌ فشل إنشاء الإيميل.")

@client.on(events.NewMessage(pattern=r'\.كتابة(?: (\d+))?'))
async def typing_fake(event):
    seconds = int(event.pattern_match.group(1) or 15)
    async with event.client.action(event.chat_id, 'typing'):
        await asyncio.sleep(seconds)
    await event.delete()

@client.on(events.NewMessage(pattern=r'\.فيد(?: (\d+))?'))
async def sending_video_fake(event):
    seconds = int(event.pattern_match.group(1) or 15)
    async with event.client.action(event.chat_id, 'video'):
        await asyncio.sleep(seconds)
    await event.delete()

@client.on(events.NewMessage(pattern=r'\.صوتية(?: (\d+))?'))
async def sending_voice_fake(event):
    seconds = int(event.pattern_match.group(1) or 15)
    async with event.client.action(event.chat_id, 'record-voice'):
        await asyncio.sleep(seconds)
    await event.delete()

# قواعد بيانات مؤقتة
enabled_replies = set()
auto_replies = {}  # {chat_id: {الكلمة: الرد}}

# ——— أمر .تقييد ———
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
import time

@client.on(events.NewMessage(pattern=r"\.تقييد ?(\d+)?"))
async def restrict_user(event):
    if not event.is_group:
        return await event.reply("❌ هذا الأمر يعمل فقط في المجموعات.")

    if not event.is_reply:
        return await event.reply("❗ قم بالرد على رسالة الشخص الذي تريد تقييده.")

    try:
        user = await event.get_reply_message()
        user_id = user.sender_id

        # عدد الدقائق (افتراضي 60 دقيقة إذا ما انطيت رقم)
        minutes = int(event.pattern_match.group(1)) if event.pattern_match.group(1) else 60
        until_time = int(time.time()) + (minutes * 60)

        rights = ChatBannedRights(
            until_date=until_time,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True,
        )

        await client(EditBannedRequest(event.chat_id, user_id, rights))
        await event.reply(f"✅ تم تقييد العضو لمدة {minutes} دقيقة.")
    except Exception as e:
        await event.reply(f"❌ فشل التقييد:\n{str(e)}")

# ——— أمر .الغاء تقييد ———
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

@client.on(events.NewMessage(pattern=r"\.الغاء تقييد$"))
async def unrestrict_user(event):
    if not event.is_group:
        return await event.reply("❌ هذا الأمر يعمل فقط في المجموعات.")

    if not event.is_reply:
        return await event.reply("❗ قم بالرد على رسالة الشخص الذي تريد فك تقييده.")

    try:
        reply = await event.get_reply_message()
        user_id = reply.sender_id

        rights = ChatBannedRights(
            until_date=None,
            send_messages=False,
            send_media=False,
            send_stickers=False,
            send_gifs=False,
            send_games=False,
            send_inline=False,
            embed_links=False,
        )

        await client(EditBannedRequest(event.chat_id, user_id, rights))
        await event.reply("✅ تم فك التقييد عن العضو.")
    except Exception as e:
        await event.reply(f"❌ لم أتمكن من فك التقييد.\n{str(e)}")

# ——— أمر .كشف المجموعة ———
@client.on(events.NewMessage(pattern=r"\.كشف المجموعة$"))
async def group_info(event):
    if event.is_group:
        chat = await event.get_chat()
        info = f"""📊 معلومات الكروب:
• الاسم: {chat.title}
• ID: {chat.id}
• عدد الأعضاء: {chat.participants_count}
• نوع الكروب: {"برايفت" if chat.megagroup else "عام"}
"""
        await event.reply(info)
    else:
        await event.reply("❗ هذا الأمر فقط في الكروبات.")

# ——— تفعيل الردود ———
@client.on(events.NewMessage(pattern=r"\.تفعيل هنا$"))
async def enable_group_replies(event):
    if event.is_group:
        enabled_replies.add(event.chat_id)
        await event.reply("✅ تم تفعيل الردود في هذا الكروب.")
    else:
        await event.reply("❗ هذا الأمر فقط في الكروبات.")

# ——— تعطيل الردود ———
@client.on(events.NewMessage(pattern=r"\.تعطيل هنا$"))
async def disable_group_replies(event):
    if event.is_group:
        enabled_replies.discard(event.chat_id)
        await event.reply("⛔ تم تعطيل الردود في هذا الكروب.")
    else:
        await event.reply("❗ هذا الأمر فقط في الكروبات.")

# ——— إضافة رد ———
@client.on(events.NewMessage(pattern=r"^\.اضف رد \+ (.+) \+ (.+)$"))
async def add_auto_reply(event):
    if event.is_group:
        chat_id = event.chat_id
        question, answer = event.pattern_match.group(1), event.pattern_match.group(2)
        if chat_id not in auto_replies:
            auto_replies[chat_id] = {}
        auto_replies[chat_id][question.lower()] = answer
        await event.reply(f"✅ تم إضافة الرد:\n\n{question} → {answer}")
    else:
        await event.reply("❗ هذا الأمر فقط داخل الكروبات.")

# ——— عرض كل الردود ———
@client.on(events.NewMessage(pattern=r"\.الردود$"))
async def show_replies(event):
    if event.is_group:
        replies = auto_replies.get(event.chat_id, {})
        if not replies:
            await event.reply("📭 لا توجد ردود مضافة في هذا الكروب.")
        else:
            text = "📚 الردود المضافة:\n"
            for i, (q, a) in enumerate(replies.items(), 1):
                text += f"\n{i}- `{q}` → `{a}`"
            await event.reply(text)
    else:
        await event.reply("❗ هذا الأمر فقط في الكروبات.")

# ——— حذف رد معين ———
@client.on(events.NewMessage(pattern=r"^\.حذف رد \+ (.+)$"))
async def delete_reply(event):
    if event.is_group:
        question = event.pattern_match.group(1).lower()
        if event.chat_id in auto_replies and question in auto_replies[event.chat_id]:
            del auto_replies[event.chat_id][question]
            await event.reply(f"🗑️ تم حذف الرد المرتبط بـ: `{question}`")
        else:
            await event.reply("⚠️ لم يتم العثور على هذا الرد.")
    else:
        await event.reply("❗ هذا الأمر فقط داخل الكروبات.")

# ——— الردود التلقائية ———
@client.on(events.NewMessage())
async def auto_reply(event):
    if event.is_group and event.chat_id in enabled_replies:
        msg = event.raw_text.lower().strip()
        replies = auto_replies.get(event.chat_id, {})
        if msg in replies:
            await event.reply(replies[msg])
from telethon import events

@client.on(events.NewMessage(pattern=r"\.اوامر الميمز"))
async def m7_command(event):
    await event.delete()
    message = """⋆─┄─┄─┄─ قائمة اوامر الميمز ─┄─┄─┄─⋆
• ︎البصمة : `.هزيمه مؤلمة`
• ︎البصمة : `.لعنه امون`
• ︎البصمة : `.ضحك 1`
• ︎البصمة : `.ضحك 2`
• ︎البصمة : `.خناجر` 
• ︎البصمة : `.زيج حزين`
• ︎البصمة : `.زيج`
• ︎البصمة : `.ام لولي`
• ︎البصمة : `.اشك هدومي`
• ︎البصمة : `.اغمضتها`
• ︎البصمة : `.خابرني عاليوتيوب`
• ︎البصمة : `.اكل خرا`

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆"""
    await event.respond(message)            

from telethon import events

@client.on(events.NewMessage(pattern=r"\.م13"))
async def m13_command(event):
    await event.delete()
    message = """⋆─┄─┄─┄─ المـيمـز والاختصارات ─┄─┄─┄─⋆

 ⎉╎`.اضف بصمه + الكلمة` | بالرد 
✶ الامر اضف او حذف الاضافة بصمه 

 ⎉╎ `.اوامر الميمز` 
✶  يعرض قائمة بصمات الميمز الجاهزة

⎉╎ `.اختصار + كلمة` | بالرد 
✶  يقوم بأضافة اختصار للكلمه 

⎉╎ `.حذف اختصار + الاختصار المضاف`
✶ يقوم بحذف الاختصار المضاف

⎉╎ `.حذف اختصاراتي` 
✶ يقوم بحذف كل الاختصارات 

⎉╎ `.اختصاراتي` 
✶ يعرض قائمة اختصاراتك 

⎉╎ `.تشغيل الاختصارات` 
✶ الامر تشغيل او تعطيل يقوم بايقاف او تشغيل الاختصارات 

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆"""
    await event.respond(message)

@client.on(events.NewMessage(pattern=r"\.م14"))
async def m14_command(event):
    await event.delete()
    message = """⋆─┄─┄─┄─ اوامــر التخصيص ─┄─┄─┄─⋆

⎉╎`.تعيين صورة الفحص` | `.حذف صورة الفحص` 
✶ يستخدم بالرد على اي صورة او فيديو او متحركة وسيظهر بعد كتابة .فحص

⎉╎ `.تعيين كليشة الفحص`   | `.حذف كليشة الفحص` 
✶ يستخدم بالرد على اي رسالة نصية وسيظهر بعد كتابة .فحص

⎉╎`.تعيين كليشة الحماية`  | `.حذف كليشة الحماية` 
✶  يستخدم بالرد على اي رسالة نصية وسيظهر بعد تفعيل الحماية 

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆"""
    await event.respond(message)

@client.on(events.NewMessage(pattern=r"\.م12"))
async def m7_command(event):
    await event.delete()
    message = """⋆─┄─┄─┄─ المـغادرة والتـصفية ─┄─┄─┄─⋆

 ⎉╎`.مغادرة القنوات`
✶ لمغادرة جميع القنوات التي تمتلكها باستثناء القنوات التي انت مالكها او مشرف فيها 

 ⎉╎ `.مغادرة الكروبات`
✶ لمغادرة جميع المجموعات باستثناء المجموعات التي انت مالكها او مشرف فيها

⎉╎ `.تصفيه البوتات`
✶ يقوم بحذف وحظر كل البوتات بالحساب 

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆"""
    await event.respond(message)
from telethon import events

@client.on(events.NewMessage(pattern=r"\.م8"))
async def m7_command(event):
    await event.delete()
    message = """⋆─┄─┄─┄─  النشــر التلقــائي ─┄─┄─┄─⋆

 ⎉╎ `.نشر` عدد الثواني معرف الكروب :
✶ للنشر في المجموعة التي وضعت معرفها مع عدد الثواني

 ⎉╎ `.نشر_كروبات` عدد الثواني : 
✶ للنشر في جميع المجموعات الموجوده في حسابك
 
 ⎉╎ `.سوبر` عدد الثواني : 
✶ للنشر بكافة المجموعات السوبر التي منظم اليها 

 ⎉╎ `.تناوب` عدد الثواني : 
✶ للنشر في جميع المجموعات بالتناوب وحسب الوقت المحدد 

 ⎉╎`.خاص` : 
✶ للنشر في جميع المحادثات الخاصة مرة واحدة فقط

 ⎉╎ `.نقط` عدد الثواني : 
✶ للرد على نفس الرسالة ب (.) وحسب الوقت المحدد 

 ⎉╎ `.مكرر` عدد الثواني : 
✶ لتكرار نفس الرسالة وحسب الوقت المحدد 

 ⎉╎`.وسبام` :
✶ يرسل الجملة كلمة بعد كلمة

 ⎉╎ `.ايقاف النشر` :
✶ لأيقاف جميع انواع النشر اعلاه

• مُـلاحظة : جميع الأوامر اعلاه تستخدم بالرد على الرسالة او الكليشة المُراد نشرها

• مُـلاحظة : جميع الأوامر اعلاه تستقبل صورة واحدة موصوفة بنص وليس اكثر من ذلك"""
    await event.respond(message)
from telethon import events
OWNER_ID = None
commands_main = """
⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆
• `.م1`  ➪ اوامــر اليوتـيوب والـخطوط
• `.م2`  ➪ اوامــر المجمــوعــه 
• `.م3`  ➪ اوامــر الـوقتــي
• `.م4`  ➪ اوامــر حمـايــة الخــاص
• `.م5`  ➪ اوامــر التسليـه والتحشيش
• `.م6`  ➪ اوامــر المـسح والتـرفيـه
• `.م7`  ➪ اوامــر الـانتحـال و التـقليد
• `.م8`  ➪ اوامــر النشــر التلقــائي
• `.م9`  ➪ اوامــر الاشتــراك الاجبــاري
• `.م10` ➪ اوامــر الـذاتيــة و المـقيد
• `.م11` ➪ اوامــر الـتـخزين والـقـوائم
• `.م12` ➪ اوامــر المـغادرة والتـصفية
• `.م13` ➪ اوامــر المـيمـز والاختصارات
• `.م14` ➪ اوامــر التخصيص و التعيين   
⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆

"""

sections = {
    ".م1": """⋆─┄─┄─┄─ الـيوتيوب والـخطوط ─┄─┄─┄─⋆

⎉╎ تحويل النصوص إلى انماط خطوط مختلفة:

↢  `.خط غامق`   ↢ لكتابة النص بشكل غامق

↢  `.خط مشطوب`  ↢ لإظهار النص بخط مشطوب

↢  `.خط رمز`    ↢ لتحويل النص إلى رموز

↢  `.خط بايثون`   ↢ لإطلالة برمجية مميزة

↢  `.خط برنت`    ↢ شكل مطبوع انيق

⎉╎ `.يوت` 
   ↢ مع الجملة او الكلمة للبحث عن اغنية على يوتيوب

⎉╎ `.انمي` 
   ↢ سيقوم هذا الامر بعرض صورة انمي عشوائية لك

⎉╎ `.كت` 
   ↢ سيقوم هذا الامر بعرض سؤال عشوائي

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆""",

    ".م2": """⋆─┄─┄─┄─  اوامــر المجمــوعــه ─┄─┄─┄─⋆

 ⎉╎ `.تقييد` | بالرد
✶ يقوم بتقيد الشخص من المجموعة

 ⎉╎ `.الغاء تقييد` | بالرد
✶ ︎يقوم بفك التقيد من الشخص 
 
 ⎉╎ `.كشف المجموعة`
✶ ︎ يعرض لك معلومات عن الكروب

 ⎉╎ `.تفعيل هنا`
✶ ︎قم برد في داخل الكروب لكي يتم تشغيل الردود في الكروب 

 ⎉╎ `.تعطيل هنا`
✶ ︎اذا قمت بل الارسال في داخل الكروب تفعيل هنا يمكنك تعطيلها اذا لم تفعل قلا تكتب شي 

 ⎉╎ `.اضف رد`
✶ ︎مثال اضف رد + السلام عليكم + وعليكم السلام عندما شخص يكتب السلام عليكم يرد بعليكم السلام

⎉╎ `.حذف رد`
✶ يحذف الرد المضاف مثال .حذف رد + السلام عليكم 

⎉╎ `.الردود`
✶ يعرض قائمة الردود المضافة

⎉╎ `.منع كلمة + الكلمه`
✶ يقوم بمنع الكلمه المضافة ويحذفها

⎉╎ `.حذف كلمة المنع + الكلمة`
✶ يقوم بحذف كلمة المنع المضافة

⎉╎ `.قائمة الكلمات`
✶ يعرض قائمة الكلمات الممنوعة

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆""",

    ".م3": """⋆─┄─┄─┄─ اوامــر الـوقتــي ─┄─┄─┄─⋆

 ⎉╎ `.اسم وقتي`
✶ يقوم هذا الامر بعد تفعيله باضافة اسم وقتي 

 ⎉╎ `.ايقاف الاسم`
✶ يقوم هذا الامر بأيقاف الاسم الوقتي

 ⎉╎ `.بايو وقتي`
✶ يقوم هذا الامر باضافة بايو وقتي

 ⎉╎ `.ايقاف البايو`
✶ يقوم هذا الامر بأيقاف البايو الوقتي

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆""",

    ".م4": """⋆─┄─┄─┄─ حمـايــة الخــاص ─┄─┄─┄─⋆
 
 ⎉╎ `.قفل الخاص`
✶ لـ تفعيـل حمايـة الخـاص لـ حسـابك

 ⎉╎ `.فتح الخاص`
✶ لـ تعطيـل حمايـة الخـاص لـ حسـابك

 ⎉╎ `.رفض`
✶ لـ رفـض الشخـص من ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك

 ⎉╎ `.المرفوضين` 
✶ لـ حظـر الشخـص من الخـاص دون تحـذير

 ⎉╎ `.قائمة السماح`
✶ لـ عـرض قائمـة بالاشخـاص المقبـولين

 ⎉╎ `.سماح`
✶ لـ السمـاح لـ الشخـص بـ ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك بـدون تحـذير

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆""",

    ".م5": """⋆─┄─┄─┄─ التسليـه والتحشيش ─┄─┄─┄─⋆

⎉╎ `.زواج` | بالرد
 
⎉╎ `.طلاك` | بالرد

⎉╎ `.نسبتنا` + اي كلمة

⎉╎`.︎بوسة` | بالرد

 ⎉╎ `.نسبة` | اي كلمة

⎉╎ `.ايميل وهمي` 
✶ يقوم بعمل ايميل وهمي (موقت)

            ⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆

⎉╎`.قران`
✶ يرسل صوت من القران عشوائي 

⎉╎ `.تفعيل القران` 
✶ الامر + تعطيل او تفعيل لـ تفعيل القران عند ارسال شخص في المجموعة قران يرسل حسابك صوت قران

⎉╎ `.شعر`
✶ يقوم بأرسال صوت شعر عشوائي 

⎉╎ `.تفعيل الشعر` 
✶ الامر + تعطيل او تفعيل لـ تفعيل الشعر عند ارسال شخص في المجموعة شعر يرسل حسابك صوت شعر

⎉╎ `.قصيدة`
✶ يرسل قصيدة عشوائية

           ⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆
""",

    ".م7": """⋆─┄─┄─┄─   الـانتحـال و التـقليد ─┄─┄─┄─⋆

 ⎉╎ `.انتحال` | بالرد على رسالة
✶ يقوم بانتحال الشخص

  ⎉╎ `.اعادة`
✶ يرجع حسابك لوضع الطبيعي 

  ⎉╎ `.تقليد` | بالرد
✶ يقوم بتقيد رسائل الشخص 

  ⎉╎ `.ايقاف التقليد`
✶ يقوم بإيقاف تقليد الشخص

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆""",

    ".م9": """⋆─┄─┄─┄─  الاشتــراك الاجبــاري ─┄─┄─┄─⋆

 ⎉╎ `.اضافة قناة` | مع يوزر القناة
✶ يجبر الشخص على الاشتراك بالقناة المحدده لمراسلتك في الخاص

  ⎉╎ `.حذف قناة` 
✶ يقوم هذا الامر بحذف القناة المضافة كأشتراك اجباري

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆""",

    ".م10": """⋆─┄─┄─┄─ الـذاتيــة و المـقيد ─┄─┄─┄─⋆

 ⎉╎ `.ذاتية` | بالرد
✶ يستخدم لحفظ الصور والفيديوهات المؤقتة .

 ⎉╎ `.حفظ الذاتية`
✶ سيقوم هذا الامر بعد تفعيلة بحفظ الصور والفيديوهات المؤقته تلقائيا .

 ⎉╎ `.مقيد` | مع رابط المنشور
✶  يقوم هذا الامر بحفظ المنشور من القنوات المقيدة

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆""",

    ".م6": """⋆─┄─┄─┄─ المـسح والتـرفيـه ─┄─┄─┄─⋆

 ⎉╎ `.حذف رسائلي + عدد`
✶ يقوم بحذف رسائلك داخل المجموعة بالعدد المحدد

 ⎉╎ `.حذف رسائلي`
✶ يقوم بحذف كل رسائلك داخل المجموعة

⎉╎ `.اكس او`
✶ يقوم ببدء لعبة اكس او

⎉╎ .مسح | بالرد 
✶ يحذف الرسالة 
⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆""",

    ".م11": """⋆─┄─┄─┄─ الـتـخزين والـقـوائم ─┄─┄─┄─⋆

⎉╎ `.تفعيل التخزين`
✶ الامـر + تفعيل او تعطيل لـ تخـزين جميـع الرسـائل بـ كـروب التخـزين

 ⎉╎ `.قائمة قنواتي`
✶ قنواتك التي انت فيها مالك او مشرف

 ⎉╎ `.قائمة كروباتي`
✶ كروباتك التي انت فيها مالك او مشرف

⎉╎`.ايدي` او `.ا`
✶.ايدي بالـرد على رسالة الشخص لـ عـرض معلومـات الشخـص او معلوماتك

 ⎉╎`.فحص`
✶ لـ فحص قاعدة البيانات وعـرض اصـدار السورس ولغة بايثـون ومكتبة تيليثون

⎉╎ `.كشف الحساب` 
✶ يعرض عدد القنوات والبوتات في الحساب الخ

⋆─┄─┄─┄─ 𝑍 ─┄─┄─┄─⋆"""
}

@client.on(events.NewMessage(pattern=r'^\.الاوامر$'))
async def send_main_commands(event):
    global OWNER_ID
    if OWNER_ID is None:
        myself = await client.get_me()
        OWNER_ID = myself.id

    if event.sender_id != OWNER_ID:
        return

    await event.delete()
    await event.respond(commands_main)

@client.on(events.NewMessage(pattern=r'^\.م(1[0-1]?|[1-9])$'))
async def send_section(event):
    global OWNER_ID
    if OWNER_ID is None:
        myself = await client.get_me()
        OWNER_ID = myself.id

    if event.sender_id != OWNER_ID:
        return

    await event.delete()
    key = event.raw_text.strip()
    if key in sections:
        await event.respond(sections[key])
    
        
# تحميل وحفظ الإعدادات
def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except:
        return {"store_private": True, "store_groups": True}

def save_config(cfg):
    with open("config.json", "w") as f:
        json.dump(cfg, f, indent=2)

def load_groups():
    try:
        with open("groups.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_groups(grps):
    with open("groups.json", "w") as f:
        json.dump(grps, f, indent=2)

config = load_config()
groups = load_groups()

# تحقق من صلاحية مجموعة التخزين
async def is_group_valid(chat_id):
    try:
        await client(GetFullChannelRequest(chat_id))
        return True
    except (ChannelInvalidError, ChannelPrivateError):
        return False

# إنشاء مجموعة التخزين إذا لم تكن موجودة
async def create_storage_group():
    from telethon import events
    from telethon.tl.functions.channels import CreateChannelRequest
    import datetime, json

config = {"store_private": False, "store_groups": False}
groups = {}

def save_config(cfg):
    with open("config.json", "w") as f:
        json.dump(cfg, f)

def save_groups(grp):
    with open("groups.json", "w") as f:
        json.dump(grp, f)

async def is_group_valid(chat_id):
    try:
        await client.get_entity(chat_id)
        return True
    except:
        return False

# تفعيل التخزين
@client.on(events.NewMessage(pattern=r"^\.تفعيل التخزين$"))
async def enable_storage(event):
    config["store_private"] = True
    config["store_groups"] = True
    save_config(config)

    if "storage_chat_id" not in groups or not await is_group_valid(groups["storage_chat_id"]):
        result = await client(CreateChannelRequest(
            title="مجمـوعـة التخـزيـن",
            about="لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامـة (وظيفتهـا تخزيـن رسـائل الخـاص.)",
            megagroup=True
        ))
        groups["storage_chat_id"] = result.chats[0].id
        save_groups(groups)

    await client.send_message(groups["storage_chat_id"], "✅ تم تفعيل التخزين من السورس\n• By : @cfc_5\n• 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙  𝐓𝐎𝐏 1")
    await event.edit("✅ تم تفعيل التخزين.")

# تعطيل التخزين
@client.on(events.NewMessage(pattern=r"^\.تعطيل التخزين$"))
async def disable_storage(event):
    config["store_private"] = False
    config["store_groups"] = False
    save_config(config)
    await event.edit("❌ تم تعطيل التخزين.")

# تخزين رسائل الخاص
@client.on(events.NewMessage(incoming=True))
async def forward_private(event):
    if event.is_private and config.get("store_private", False):
        try:
            if "storage_chat_id" in groups:
                await client.forward_messages(groups["storage_chat_id"], event.message, event.sender_id)
        except Exception as e:
            print(f"⚠️ فشل تحويل رسالة الخاص: {e}")

# تخزين ردود الكروبات على رسائلك
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
                    msg_link = (
                        f"https://t.me/c/{str(event.chat_id)[4:]}/{event.id}"
                        if str(event.chat_id).startswith("-100") else "لا يوجد رابط"
                    )
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



@client.on(events.NewMessage(pattern=r"^\.ا(?:يدي)?$"))
async def user_info(event):
    global OWNER_ID

    # تحديد المالك تلقائيًا عند أول استخدام
    if OWNER_ID is None:
        OWNER_ID = event.sender_id
        print(f"✅ تم تعيين المالك تلقائيًا: {OWNER_ID}")

    # التحقق أن الأمر فقط للمالك
    if event.sender_id != OWNER_ID:
        return await event.respond("❌ هذا الأمر خاص بالمالك فقط.")

    if event.raw_text.strip() not in [".ا", ".ايدي"]:
        return

    try:
        await event.delete()
    except:
        pass

    replied_msg = await event.get_reply_message()
    if replied_msg:
        user = await replied_msg.get_sender()
        chat_id = replied_msg.chat_id
        reply_to_id = replied_msg.id
    else:
        user = await event.get_sender()
        chat_id = event.chat_id
        reply_to_id = None

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

    photos_count = photos.count

    try:
        msg_count = 0
        async for msg in client.iter_messages(chat_id, from_user=user.id):
            msg_count += 1
    except:
        msg_count = "؟"

    caption = f"""•⎚• مـعلومـات المسـتخـدم مـن بـوت 𝐙 
ٴ⋆─┄─┄─┄─ 𝐙 ─┄─┄─┄─⋆
✦ الاســم  ⤎ [{first_name}](tg://user?id={user_id})
✦ اليـوزر  ⤎ {username}
✦ الايـدي  ⤎ `{user_id}`
✦ الرتبــه  ⤎ {rank}
✦ الصـور  ⤎ {photos_count}
✦ الرسائل  ⤎ {msg_count}
✦ البايـو  ⤎ {bio}
ٴ⋆─┄─┄─┄─ 𝐙 ─┄─┄─┄─⋆"""

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


@client.on(events.NewMessage(pattern=r'^\.انتحال$'))
async def impersonate_user(event):
    if not event.is_edit:
        await event.edit("❌ يجب الرد على رسالة الشخص الذي تريد انتحاله.")
        return

    user_msg = await event.get_reply_message()
    sender = await user_msg.get_sender()

    me = await client.get_me()
    profile_photos = await client.get_profile_photos('me')
    original_info['first_name'] = me.first_name or ""
    original_info['last_name'] = me.last_name or ""
    
    try:
        full_me = await client(functions.users.GetFullUserRequest(me.id))
        original_info['bio'] = getattr(full_me.full_user, 'about', '')[:70]
    except:
        original_info['bio'] = ""

    original_info['photo'] = None
    if profile_photos.total > 0:
        file = await client.download_media(profile_photos[0])
        original_info['photo'] = file

    full_user = await client(functions.users.GetFullUserRequest(sender.id))
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
        file = await client.download_media(photos[0])
        await client(functions.photos.UploadProfilePhotoRequest(
            file=await client.upload_file(file)
        ))
        os.remove(file)

    await event.edit("✅ تم انتحال الحساب بنجاح.")


@client.on(events.NewMessage(pattern=r'^\.اعادة$'))
async def restore_original(event):
    if not original_info:
        await event.edit("❌ لا توجد بيانات محفوظة لإعادتها.")
        return

    await client(functions.account.UpdateProfileRequest(
        first_name=original_info['first_name'],
        last_name=original_info['last_name'],
        about=original_info['bio']
    ))

    if original_info.get('photo'):
        await client(functions.photos.UploadProfilePhotoRequest(
            file=await client.upload_file(original_info['photo'])
        ))
        os.remove(original_info['photo'])

    original_info.clear()
    await event.edit("✅ تمت إعادة الحساب إلى شكله السابق.")


@client.on(events.NewMessage(outgoing=True, pattern=r"\.رسائلي$"))
async def my_messages(event):
    count = 0
    async for message in client.iter_messages(event.chat_id, from_user='me'):
        count += 1
    await event.edit(f"📨 عدد رسائلك في هذه المحادثة: {count}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.رسائله$"))
async def his_messages(event):
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



import os
import json
import time
import datetime
import platform
from telethon import events

start_time = datetime.datetime.now()

# ملف حفظ البيانات
FOLDER = "data"
os.makedirs(FOLDER, exist_ok=True)
FILE_PATH = os.path.join(FOLDER, "f7.json")

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        f7_data = json.load(f)
else:
    f7_data = {}

def save_f7():
    with open(FILE_PATH, "w") as f:
        json.dump(f7_data, f)

@client.on(events.NewMessage(pattern=r'^\.فحص$'))
async def ping(event):
    await event.delete()

    start = time.perf_counter()
    temp = await event.respond("انتظر .")
    end = time.perf_counter()
    ping_time = round((end - start) * 1000)

    user = await event.client.get_me()
    full_name = f"[{user.first_name}](tg://user?id={user.id})"
    pyver = platform.python_version()
    uptime = datetime.datetime.now() - start_time
    uptime_str = str(uptime).split('.')[0]

    await temp.delete()

    data = f7_data.get(str(user.id), {})
    message_template = data.get("text", (
        "┏━━━━━━━━━━━━━━━┓\n"
        "┃ ✦ 𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁 : `{pyver}`\n"
        "┃ ✦ 𝙸𝙳 : `{user.id}`\n"
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
            user=user,
            full_name=full_name
        )
    except Exception as e:
        return await event.reply(f"❌ خطأ في الكليشة:\n{e}")

    image_path = data.get("image")

    if image_path and os.path.exists(image_path):
        await client.send_file(event.chat_id, image_path, caption=message, parse_mode='md')
    else:
        await event.respond(message, parse_mode='md')


# تعيين كليشة الفحص (للمالك فقط)
@client.on(events.NewMessage(pattern=r'^\.تعيين كليشة الفحص$'))
async def set_f7_text(event):
    owner_id = (await client.get_me()).id
    if event.sender_id != owner_id:
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


# تعيين صورة الفحص (للمالك فقط)
@client.on(events.NewMessage(pattern=r'^\.تعيين صورة الفحص$'))
async def set_f7_image(event):
    owner_id = (await client.get_me()).id
    if event.sender_id != owner_id:
        return await event.reply("❌ هذا الأمر يخص المالك فقط.")

    user_id = str(event.sender_id)
    reply = await event.get_reply_message()

    if not reply or not reply.photo:
        return await event.edit("❌ يجب الرد على صورة لتعيينها للفحص.")

    path = await reply.download_media(file=FOLDER + f"/f7_{user_id}.jpg")

    if user_id not in f7_data:
        f7_data[user_id] = {}

    f7_data[user_id]["image"] = path
    save_f7()
    await event.edit("✅ تم حفظ صورة الفحص.")


# حذف كليشة الفحص (للمالك فقط)
@client.on(events.NewMessage(pattern=r'^\.حذف كليشة الفحص$'))
async def delete_f7_text(event):
    owner_id = (await client.get_me()).id
    if event.sender_id != owner_id:
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


# حذف صورة الفحص (للمالك فقط)
@client.on(events.NewMessage(pattern=r'^\.حذف صورة الفحص$'))
async def delete_f7_image(event):
    owner_id = (await client.get_me()).id
    if event.sender_id != owner_id:
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




@client.on(events.NewMessage(outgoing=True, pattern=r'\.يوت (.+)'))
async def yt_audio(event):
    chat = event.chat_id
    query = event.pattern_match.group(1).strip()

    if query.startswith("."):
        query = query[1:]

    full_query = "يوت " + query
    await event.edit("⏳ يرجى الانتظار، جاري التحميل...")

    try:
        async with client.conversation('@l_XI_ibot') as conv:
            await conv.send_message(full_query)

            audio_clip = None
            timeout = 20
            start_time = asyncio.get_event_loop().time()

            while asyncio.get_event_loop().time() - start_time < timeout:
                try:
                    response = await conv.get_response()
                    await client.send_read_acknowledge(conv.chat_id)

                    if "عليك الأشتراك" in response.message:
                        try:
                            channel_name = re.search(r"قناة البوت : (@\w+)", response.message).group(1)
                            await client(JoinChannelRequest(channel_name))
                            await conv.send_message(full_query)
                            continue
                        except:
                            await event.edit("❗️ لم أتمكن من الاشتراك في القناة المطلوبة.")
                            return

                    if response.audio:
                        audio_clip = response
                        break

                except asyncio.TimeoutError:
                    break

        if audio_clip:
            await client.send_file(chat, file=audio_clip.media, silent=True)
            await event.delete()
        else:
            await event.edit("❗️المحتوى غير موجود أو لم يتم الرد في الوقت المحدد.")

    except Exception as e:
        await event.edit(f"⚠️ حدث خطأ أثناء التحميل: {e}")

    # حذف المحادثة مع البوت
    try:
        await client(DeleteHistoryRequest(peer='@l_XI_ibot', max_id=0, just_clear=False, revoke=True))
    except Exception as e:
        print(f"فشل حذف المحادثة: {e}")

# الدالة الرئيسية لتشغيل البوت
async def main():
    await client.start()
    await create_storage_group()
    print("✅ تم تسجيل الدخول بنجاح.")
    print("🤖 البوت شغّال الآن، ارسل .ا أو .ايدي أو .انتحال أو .اعادة أو .رسائلي أو .رسائله أو .فحص")
    await client.run_until_disconnected()
from telethon import TelegramClient, events
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.users import GetFullUserRequest

import os
import json
from telethon import events
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.users import GetFullUserRequest

# مسار حفظ الكليشة
DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)
PROTECT_FILE = os.path.join(DATA_FOLDER, "protect_msg.json")

# كليشة افتراضية
DEFAULT_PROTECTION_MESSAGE = (
    "━ 𝐀𝐔𝐓𝐎 𝐑𝐄𝐏𝐋𝐘 - الرد الآلــي 💪\n"
    "•─────────────────•\n\n"
    "❞ مرحبًـا  {name} ❝\n\n"
    "⤶ قد اكـون مشغـول أو غيـر موجـود حاليـًا ؟!\n"
    "⤶ ❨ هذه رسالتك رقم {remaining} مـن {max} المسموحة ⚠️❩\n"
    "⤶ لا تقـم بـ إزعاجـي وفي حال أزعجتني سـوف يتم حظـرك تلقائيًا . . .\n\n"
    "⤶ فقط قل سبب مجيئك وانتظـر الـرد ⏳"
)

# تحميل الكليشة من الملف أو اعادة الافتراضي
def load_protection_message():
    if os.path.exists(PROTECT_FILE):
        try:
            with open(PROTECT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("message", DEFAULT_PROTECTION_MESSAGE)
        except:
            pass
    return DEFAULT_PROTECTION_MESSAGE

# حفظ الكليشة في ملف
def save_protection_message(message):
    with open(PROTECT_FILE, "w", encoding="utf-8") as f:
        json.dump({"message": message}, f, ensure_ascii=False)

# حذف ملف الكليشة (استعادة الافتراضي)
def delete_protection_message_file():
    if os.path.exists(PROTECT_FILE):
        os.remove(PROTECT_FILE)

# المتغيرات العامة
OWNER_ID = None
PRIVATE_LOCK = False
ALLOWED_USERS = set()
USER_MESSAGE_COUNT = {}
BLOCKED_USERS = set()
MAX_MESSAGES = 7
PROTECTION_MESSAGE_TEMPLATE = load_protection_message()

# دالة التحقق من المالك
async def is_owner(event):
    global OWNER_ID
    if OWNER_ID is None:
        OWNER_ID = (await event.client.get_me()).id
    return event.sender_id == OWNER_ID

# أوامر التحكم

@client.on(events.NewMessage(pattern=r"^\.قفل الخاص$"))
async def lock_private(event):
    if not await is_owner(event): return
    global PRIVATE_LOCK
    PRIVATE_LOCK = True
    await event.reply("🔒 تم تفعيل قفل الخاص.")

@client.on(events.NewMessage(pattern=r"^\.فتح الخاص$"))
async def unlock_private(event):
    if not await is_owner(event): return
    global PRIVATE_LOCK, USER_MESSAGE_COUNT, BLOCKED_USERS
    PRIVATE_LOCK = False
    USER_MESSAGE_COUNT.clear()
    BLOCKED_USERS.clear()
    await event.reply("✅ تم فتح الخاص وتصفير العدادات.")

@client.on(events.NewMessage(pattern=r"^\.تحديد الانذارات (\d+)$"))
async def set_max_warnings(event):
    if not await is_owner(event): return
    global MAX_MESSAGES
    MAX_MESSAGES = int(event.pattern_match.group(1))
    await event.edit(f"⚙️ تم تعيين عدد الإنذارات إلى: {MAX_MESSAGES}")

@client.on(events.NewMessage(pattern=r"^\.تعيين كليشة الحماية$"))
async def set_protection_message(event):
    if not await is_owner(event): return
    global PROTECTION_MESSAGE_TEMPLATE
    if not event.is_reply:
        return await event.reply("❗️الرجاء الرد على رسالة تحتوي على الكليشة.")
    reply = await event.get_reply_message()
    if not reply.message:
        return await event.reply("❗️الرسالة المردود عليها لا تحتوي على نص.")
    PROTECTION_MESSAGE_TEMPLATE = reply.message
    save_protection_message(PROTECTION_MESSAGE_TEMPLATE)
    await event.edit("✅ تم تحديث كليشة الحماية.")

@client.on(events.NewMessage(pattern=r"^\.حذف كليشة الحماية$"))
async def delete_protection_message_cmd(event):
    if not await is_owner(event): return
    global PROTECTION_MESSAGE_TEMPLATE
    delete_protection_message_file()
    PROTECTION_MESSAGE_TEMPLATE = DEFAULT_PROTECTION_MESSAGE
    await event.reply("🗑️ تم حذف كليشة الحماية وأُعيدت الكليشة الافتراضية.")

@client.on(events.NewMessage(pattern=r"^\.سماح$"))
async def allow_user(event):
    if not await is_owner(event): return
    if not event.is_reply:
        return await event.reply("❗️الرجاء الرد على رسالة الشخص المراد السماح له.")
    reply = await event.get_reply_message()
    user_id = reply.sender_id
    ALLOWED_USERS.add(user_id)
    USER_MESSAGE_COUNT.pop(user_id, None)
    await event.reply(f"✅ تم السماح لـ [ {user_id} ] بإرسال الرسائل بحرية.")

@client.on(events.NewMessage(pattern=r"^\.رفض$"))
async def disallow_user(event):
    if not await is_owner(event): return
    if not event.is_reply:
        return await event.reply("❗️الرجاء الرد على رسالة الشخص المراد رفضه.")
    reply = await event.get_reply_message()
    user_id = reply.sender_id
    ALLOWED_USERS.discard(user_id)
    await event.reply(f"🚫 تم رفض المستخدم [ {user_id} ].")

@client.on(events.NewMessage(pattern=r"^\.المرفوضين$"))
async def show_blocked_users(event):
    if not await is_owner(event): return
    if not BLOCKED_USERS:
        return await event.reply("✅ لا يوجد أي مستخدمين محظورين.")
    result = "🚫 قائمة المرفوضين:\n"
    for user_id in BLOCKED_USERS:
        try:
            user = await client(GetFullUserRequest(user_id))
            name = user.users[0].first_name
            result += f"• [{name}](tg://user?id={user_id})\n"
        except:
            result += f"• [User ID: {user_id}]\n"
    await event.reply(result, link_preview=False)

@client.on(events.NewMessage(pattern=r"^\.قائمة السماح$"))
async def show_allowed_users(event):
    if not await is_owner(event): return
    if not ALLOWED_USERS:
        return await event.reply("📭 لا يوجد أي مستخدم في قائمة السماح.")
    result = "✅ قائمة المستخدمين المسموح لهم:\n"
    for user_id in ALLOWED_USERS:
        try:
            user = await client(GetFullUserRequest(user_id))
            name = user.users[0].first_name
            result += f"• [{name}](tg://user?id={user_id})\n"
        except:
            result += f"• [User ID: {user_id}]\n"
    await event.reply(result, link_preview=False)

# نظام الحماية الأساسي

@client.on(events.NewMessage(incoming=True))
async def private_control(event):
    if not event.is_private:
        return
    sender = await event.get_sender()
    user_id = sender.id
    me = await client.get_me()
    if user_id == me.id or not PRIVATE_LOCK or user_id in ALLOWED_USERS:
        return
    USER_MESSAGE_COUNT[user_id] = USER_MESSAGE_COUNT.get(user_id, 0) + 1
    count = USER_MESSAGE_COUNT[user_id]
    if count > MAX_MESSAGES:
        await event.respond("🚫 لقد تجاوزت الحد المسموح من الرسائل.\n📵 تم حظرك تلقائيًا.")
        await client(BlockRequest(user_id))
        BLOCKED_USERS.add(user_id)
        return
    if PROTECTION_MESSAGE_TEMPLATE:
        await event.respond(PROTECTION_MESSAGE_TEMPLATE.format(
            name=sender.first_name or "صديقي",
            remaining=count,
            max=MAX_MESSAGES
        ))

           

from telethon import events, types
import asyncio
import re
import os

# متغير لتفعيل الحفظ التلقائي
save_self_destruct = False

# الخطوط
# تعريف الآيدي
owner_id = None

async def is_owner(event):
    global owner_id
    if owner_id is None:
        me = await client.get_me()
        owner_id = me.id
    return event.sender_id == owner_id

active_font = None

@client.on(events.NewMessage(pattern=r"\.(خط غامق|خط مشطوب|خط رمز|خط بايثون|خط برنت)"))
async def text_styles(event):
    if not await is_owner(event):
        return

    global active_font
    cmd = event.pattern_match.group(1)

    if active_font == cmd:
        active_font = None
        return await event.edit("✅ تم إيقاف تنسيق الخط.")

    active_font = cmd
    await event.edit(f"✅ تم تفعيل `{cmd}`.\nاكتب أي رسالة وسيتم تنسيقها.\n🔁 أرسل نفس الأمر لإيقافه.")

@client.on(events.NewMessage())
async def auto_font(event):
    if not await is_owner(event):
        return

    global active_font
    if not event.out or not active_font:
        return

    text = event.raw_text
    if event.pattern_match or text.startswith("."):
        return

    style = active_font
    if style == "خط غامق":
        styled = f"**{text}**"
    elif style == "خط مشطوب":
        styled = f"~~{text}~~"
    elif style == "خط رمز":
        styled = f"`{text}`"
    elif style == "خط بايثون":
        styled = f"```python\n{text}```"
    elif style == "خط برنت":
        styled = f"```{text}```"
    else:
        return

    await event.edit(styled)



import os
from telethon import events

SAVE_PATH = "temp_self_media"
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

save_self_destruct = False  # الحالة التلقائية

# أمر تفعيل/تعطيل الحفظ التلقائي
@client.on(events.NewMessage(pattern=r"\.حفظ الذاتية"))
async def toggle_auto_save(event):
    global save_self_destruct
    save_self_destruct = not save_self_destruct
    state = "مفعل ✅" if save_self_destruct else "متوقف ❌"
    await event.edit(f"📥 الحفظ التلقائي للذاتية: {state}")

# أمر يدوي .ذاتية
@client.on(events.NewMessage(pattern=r"\.ذاتية"))
async def save_self_destruct_once(event):
    reply = await event.get_reply_message()
    if not reply or not reply.media:
        return await event.reply("↯ يجب الرد على صورة أو فيديو ذاتي التدمير.")
    if not getattr(reply.media, "ttl_seconds", None):
        return await event.reply("↯ هذه الوسائط ليست مؤقتة/ذاتية التدمير.")

    try:
        path = await reply.download_media(file=SAVE_PATH)
        sender = await reply.get_sender()
        sender_name = f"[{sender.first_name}](tg://user?id={sender.id})"
        caption = (
            "ᯓ 𝗦𝗼𝘂𝗿𝗰𝗲 - حفـظ الذاتـيـة  .\n"
            "⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n"
            "𝑍╎مࢪحبـًا عـزيـزي المـالك\n"
            "𝑍╎ تـم حفـظ الذاتيـة تلقائيـًا .. بنجـاح  \n"
            f"𝑍╎المرسـل: {sender_name}"
        )
        await client.send_file("me", path, caption=caption, link_preview=False)
        os.remove(path)
        await event.edit("✅ تم حفظ الوسائط المؤقتة.")
    except Exception as e:
        await event.reply(f"❌ فشل الحفظ: {e}")

# الحفظ التلقائي للوسائط المؤقتة عند استلامها
@client.on(events.NewMessage(incoming=True))
async def auto_save_self_destruct(event):
    global save_self_destruct
    if not save_self_destruct:
        return
    if not event.media:
        return
    if not getattr(event.media, "ttl_seconds", None):
        return

    try:
        path = await event.download_media(file=SAVE_PATH)
        sender = await event.get_sender()
        sender_name = f"[{sender.first_name}](tg://user?id={sender.id})"
        caption = (
            "ᯓ 𝗦𝗼𝘂𝗿𝗰𝗲 - حفـظ الذاتـيـة  .\n"
            "⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n"
            "𝑍╎مࢪحبـًا عـزيـزي المـالك\n"
            "𝑍╎ تـم حفـظ الذاتيـة تلقائيـًا .. بنجـاح  \n"
            f"𝑍╎المرسـل: {sender_name}"
        )
        await client.send_file("me", path, caption=caption, link_preview=False)
        os.remove(path)
    except Exception as e:
        print(f"❌ فشل الحفظ التلقائي: {e}")

# قنوات المستخدم
@client.on(events.NewMessage(pattern=r"\.قائمة قنواتي"))
async def list_my_channels(event):
    result = ""
    async for dialog in client.iter_dialogs():
        entity = dialog.entity
        if getattr(entity, "broadcast", False) and getattr(entity, "creator", False):
            result += f"• {dialog.name}\n"
    await event.edit(result or "❌ لا توجد قنوات تملكها.")

# كروبات أنت مشرف بها
@client.on(events.NewMessage(pattern=r"\.قائمة كروباتي"))
async def list_my_groups(event):
    result = ""
    async for dialog in client.iter_dialogs():
        if dialog.is_group and dialog.entity.admin_rights:
            result += f"• {dialog.name}\n"
    await event.edit(result or "❌ لا توجد مجموعات أنت مشرف بها.")


# تهيئة المتغير العالمي للخط
active_font = None
# بدء تشغيل العميل
print("@cfc_5")
client.start()
print("سورس Z يعمل ينجاح")
client.run_until_disconnected()

if name == 'main':
    asyncio.run(main())
