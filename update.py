from telethon import events
import asyncio
import os
import sys
import shutil
import requests
import zipfile

from config import client

ZIP_URL = "https://github.com/im7zo/Z-top-1/archive/refs/heads/main.zip"
ZIP_FILE = "source_update.zip"
TEMP_EXTRACTED = "Z-top-1-main"
TARGET_FOLDER = "Z"

PROTECTED_FILES = ["config.py"]
PROTECTED_EXTENSIONS = [".session", ".session-journal"]

@client.on(events.NewMessage(pattern=r'^\.تحديث$'))
async def update_all(event):
    msg = await event.reply(
        "ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐙 🝢 إعــادة التشغيــل\n"
        "•─────────────────•\n\n"
        "⇜ جـارِ إعـادة تشغيـل بـوت 𝐙 . . .🌐\n\n"
        "%0 ▭▭▭▭▭▭▭▭▭▭"
    )

    try:
        # تحميل التحديث
        r = requests.get(ZIP_URL)
        with open(ZIP_FILE, "wb") as f:
            f.write(r.content)

        for i in range(20, 61, 20):
            bar = "▬" * (i // 10) + "▭" * ((100 - i) // 10)
            await msg.edit(
                f"ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐙 🝢 إعــادة التشغيــل\n"
                f"•─────────────────•\n\n"
                f"⇜ جـارِ إعـادة تشغيـل بـوت 𝐙 . . .🌐\n\n"
                f"%{i} {bar}"
            )
            await asyncio.sleep(0.5)

        # فك الضغط
        with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall()

        # حذف مجلد Z القديم إذا موجود
        if os.path.exists(TARGET_FOLDER):
            shutil.rmtree(TARGET_FOLDER)

        os.makedirs(TARGET_FOLDER, exist_ok=True)

        # نسخ كل شيء من Z-top-1-main إلى Z
        for item in os.listdir(TEMP_EXTRACTED):
            src = os.path.join(TEMP_EXTRACTED, item)
            dst = os.path.join(TARGET_FOLDER, item)

            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)

        # تنظيف الملفات المؤقتة
        os.remove(ZIP_FILE)
        shutil.rmtree(TEMP_EXTRACTED)

        for i in range(80, 101, 20):
            bar = "▬" * (i // 10) + "▭" * ((100 - i) // 10)
            await msg.edit(
                f"ᯓ 𝗦𝗢𝗨𝗥𝗖𝗘 𝐙 🝢 إعــادة التشغيــل\n"
                f"•─────────────────•\n\n"
                f"⇜ جـارِ إعـادة تشغيـل بـوت 𝐙 . . .🌐\n\n"
                f"%{i} {bar}"
            )
            await asyncio.sleep(0.5)

        await msg.edit("""•⎆┊أهـلًا عـزيـزي 
•⎆┊يتـم الآن إعــادة تشغيـل بـوت 𝐙
•⎆┊قـد يستغـرق الأمـــر 2-1 دقائـق ▬▭ ...""")
        await asyncio.sleep(1)

        os.execv(sys.executable, [sys.executable] + sys.argv)

    except Exception as e:
        await msg.edit(f"❌ حدث خطأ أثناء التحديث:\n`{str(e)}`")