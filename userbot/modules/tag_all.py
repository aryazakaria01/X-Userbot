import re
from userbot import CMD_HELP, bot
from userbot.events import xubot_cmd
from userbot import CUSTOM_CMD as xcm

usernexp = re.compile(r"@(\w{3,32})\[(.+?)\]")
nameexp = re.compile(r"\[([\w\S]+)\]\(tg://user\?id=(\d+)\)\[(.+?)\]")


@bot.on(xubot_cmd(outgoing=True, pattern=r"all(?: |$)(.*)"))
async def all(event):
    if event.fwd_from:
        return
    await event.delete()
    query = event.pattern_match.group(1)
    mentions = f"@all {query}"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 1000):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await bot.send_message(chat, mentions, reply_to=event.message.reply_to_msg_id)


CMD_HELP.update({
    "tag_all":
    f"`{xcm}all`\
\nUsage: Untuk Mengetag semua anggota yang ada di group."
})
