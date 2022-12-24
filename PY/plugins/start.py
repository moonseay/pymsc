from PY import PY, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
*Hello {} !*
◍ ɪᴍ ᴘʏ ᴍᴜꜱɪᴄ ʙᴏᴛ [🏆](https://telegra.ph/file/13f20a7ba6474db2b81ee.jpg)
────────────────────────
✪ ꜱᴀᴛᴀ ʙɪꜱᴀ ᴍᴇᴍᴜᴛᴀʀ ᴍᴜꜱɪᴄ ᴅᴀɴ ᴠɪᴅᴇᴏ
✪ sᴀʏᴀ ᴘᴜɴʏᴀ ʙᴀɴʏᴀᴋ ꜰɪᴛᴜʀ ʏᴀɴɢ ᴀɴᴅᴀ sᴜᴋᴀ
────────────────────────
◍ ᴛᴇᴋᴀɴ /help ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴘᴇʀɪɴᴛᴀʜ sᴀʏᴀ ʏᴀɴɢ ᴛᴇʀsᴇᴅɪᴀ.
"""

@PY.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", "https://t.me/tr4shcode")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ✅**")
       return



@PY.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", "https://telegra.ph/file/d25ba9bdcb28b1104fd57.jpg")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return
