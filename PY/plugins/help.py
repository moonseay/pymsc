from telethon import events, Button
from PY import PY, BOT_USERNAME
from Config import Config


btn =[
    [Button.inline("Admin", data="admin"), Button.inline("Bans", data="bans")],
    [Button.inline("Pins", data="pins"), Button.inline("Pugres", data="purges")],
    [Button.inline("Play", data="play"), Button.inline("Chat Cleaner", data="zombies")],
    [Button.inline("Locks", data="locks"), Button.inline("Misc", data="misc")],
    [Button.inline("Home", data="start")]]

HELP_TEXT = "Welcome To help Menu Section\n\nClick on the Buttons!"


@PY.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_group:
       await event.reply("Contact me in PM to get available help menu!", buttons=[
       [Button.url("Help And Commands!", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@PY.on(events.NewMessage(pattern="^/start help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.reply(HELP_TEXT, buttons=btn)

@PY.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.edit(HELP_TEXT, buttons=btn)
