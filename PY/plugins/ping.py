import os

from telethon import Button, events

from PY import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/96a0d61911707da5be872.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@moonseay"
)

CAPTION = f"**ping**\n\n   ⚜ {ms}\n   Master ~『{ALIVE}』"


@PY.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("Channel", "https://t.me/tr4shcode")]]
    await PY.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
