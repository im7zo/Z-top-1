import os
import sys
import subprocess

# تثبيت المكتبات المطلوبة إن لم تكن مثبتة
def silent_install(package):
    try:
        __import__(package)
    except ImportError:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except Exception as e:
            print(f"❌ فشل تثبيت {package}: {e}")

# الحزم الضرورية لتشغيل السورس
packages = [
    "telethon",
    "requests",
    "aiohttp",
    "pytz",
    "gtts"  
]

for pkg in packages:
    silent_install(pkg)

# بعد التأكد من وجود الحزم
import asyncio
from config import client

# استيراد الأوامر من مجلد Z
from Z import (
    account_info,
    admen_clo,
    Auto,
    bb,
    im,
    kat,
    kt,
    memes,
    mmo,
    name,
    ns,
    quran,
    rt,
    st,
    ui,
    veo,
    we,
    yot_tt,
    create_groups,
    hunt,         # ملف صيد اليوزرات
    auto_zar,
    story,
    media,
    voice_tts,
    zzz,
    encrypt_rools,
    ping,
    rev,
    afk,
    players,
    randomm,
    sd,
    kick,
    lovelyrun,
    fack,
    sah,
   goodnight
)

# تشغيل السورس
print(r"""
⣿⣿⣿⣿⣿⢿⠛⢛⠿⠉⠉⠉⡉⢙⣻⠻⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠟⢁⡠⠀⠄⠀⠀⠀⠉⠙⠒⠃⠾⠹⣲⡘⠿⣿⣿⣿
⣿⡿⠁⠀⠀⠀⠈⠛⠚⠉⠉⠛⠉⠙⠳⠖⣤⢌⡑⠂⠞⢿⣿
⡟⠐⠂⠅⡠⠂⠁⠀⠀⢀⣴⣦⣶⣶⣶⣦⣌⠘⢮⡔⡈⠙⣿
⠁⢀⠄⡈⠄⢀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⡆⠈⢣⠈⠜⣿
⠄⠑⡨⠈⠀⢠⣴⠿⡿⣿⣿⣿⣿⣿⣿⡿⠟⠻⡄⠈⢸⡀⠚
⡤⠪⠀⠀⢠⣿⣥⡴⠦⠤⠉⣙⣿⣿⠡⡔⠾⠟⣾⠀⠨⢀⠘
⠃⠀⠀⠀⢸⣿⣤⡠⠧⢤⡻⢼⣿⣿⣼⣿⣤⣧⣿⠀⡄⢸⠀
⠀⣀⠀⠀⠀⣿⣿⣿⣷⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡄⢀⢸⠀
⠠⡇⠀⠀⠀⢹⣿⡿⣿⣿⣏⡖⢿⣿⢓⣽⣿⣿⣿⠁⢨⢸⠀
⠠⠇⠀⠀⠀⠀⠫⣿⣿⠟⠉⠀⠀⠄⠀⠉⠙⢿⡟⠀⠈⠸⠀
⡐⡆⠀⠀⠀⠀⠀⠘⠁⠀⢀⡐⠒⠒⠢⠂⠀⠀⠂⠀⢀⠀⠀
⣹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢰
⢺⠀⠀⠀⠈⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡘
⡎⠀⠀⠀⠀⠄⣇⠠⢄⠀⠀⠀⠀⠀⠀⣀⡀⡄⠀⠀⠀⠀⡇
⠄⠀⠀⠀⠀⡇⣷⡀⠩⡇⣠⣮⣶⣿⠿⣫⡾⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⣷⠑⠳⠋⣾⡿⠟⣫⢵⡿⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠐⠁⢀⣴⠀⣩⡖⡽⠝⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣴⡏⣫⣾⠟⠉⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⢟⠕⠋⢀⣠⣲⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⣷⠋⣠⠞⣰⣿⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠁⣼⡟⣼⡏⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢁⣾⣯⢃⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⢤⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣲⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡿⣜⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡟⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣽⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

async def main():
    print("          𝙳𝙴𝚅          𝚉\n          𝙳𝙴𝚅      @𝚌𝚏𝚌_𝟻")
    await client.start()
    await client.run_until_disconnected()

# بدء التنفيذ
if __name__ == "__main__":
    asyncio.run(main())