from telethon import events
from config import client  # استيراد الكلاينت من config

@client.on(events.NewMessage(pattern=r"\.تجربة التحديث"))
async def commands_menu(event):
    await event.respond(
        "✅ التحديث يعمل بنجاح!",
        link_preview=False
    )