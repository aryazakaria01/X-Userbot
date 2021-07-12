# Thank you to @Badboyanim for this module
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import CMD_HELP

chat = "@gamee"


@register(outgoing=True, pattern="^.ninjagame ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()
    else:
        await event.delete()
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("play grafit ninja 2")
            await event.delete()
            audio = await conv.get_response()
            await event.delete()
            audio = await conv.get_response()
            await event.delete()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete(event.chat_id, audio)
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("play grafit ninja 2")
            await event.delete()
            audio = await conv.get_response()
            await event.delete()
            audio = await conv.get_response()
            await event.delete()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete(event.chat_id, audio)


@register(outgoing=True, pattern="^.racergame ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()
    else:
        await event.delete()
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("Play - F1 Racer")
            await event.delete()
            audio = await conv.get_response()
            await event.delete()
            audio = await conv.get_response()
            await event.delete()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("Play - F1 Racer")
            await event.delete()
            audio = await conv.get_response()
            await event.delete()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()


CMD_HELP.update(
    {
        "gamealpha": "`.ninjagame dan .racergame`\
    \nNinja Game."
    })
