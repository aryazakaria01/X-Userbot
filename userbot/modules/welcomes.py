from datetime import datetime

from pytz import timezone
from userbot.events import xubot_cmd
from userbot import CUSTOM_CMD as xcm
from userbot import CMD_HELP, bot, LOGS, CLEAN_WELCOME, BOTLOG_CHATID
from telethon.events import ChatAction


@bot.on(ChatAction)
async def welcome_to_chat(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import get_current_welcome_settings
        from userbot.modules.sql_helper.welcome_sql import update_previous_welcome
    except AttributeError:
        return
    cws = get_current_welcome_settings(event.chat_id)
    if cws:
        """user_added=True,
        user_joined=True,
        user_left=False,
        user_kicked=False"""
        if (event.user_joined
                or event.user_added) and not (await event.get_user()).bot:
            if CLEAN_WELCOME:
                try:
                    await event.client.delete_messages(event.chat_id,
                                                       cws.previous_welcome)
                except Exception as e:
                    LOGS.warn(str(e))
            a_user = await event.get_user()
            chat = await event.get_chat()
            me = await event.client.get_me()

            # Current time in UTC
            now_utc = datetime.now(timezone("UTC"))

            # Convert to Jakarta time zone
            jakarta_timezone = now_utc.astimezone(timezone("Asia/Jakarta"))
            if jakarta_timezone.hour < 4:
                pass
            elif 4 <= jakarta_timezone.hour < 6:
                pass
            elif 6 <= jakarta_timezone.hour < 11:
                pass
            elif 11 <= jakarta_timezone.hour < 13:
                pass
            elif 13 <= jakarta_timezone.hour < 15:
                pass
            elif 15 <= jakarta_timezone.hour < 17:
                pass
            elif 17 <= jakarta_timezone.hour < 19:
                pass
            else:
                pass

            title = chat.title if chat.title else "this chat"
            participants = await event.client.get_participants(chat)
            count = len(participants)
            mention = "[{}](tg://user?id={})".format(a_user.first_name,
                                                     a_user.id)
            my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
            first = a_user.first_name
            last = a_user.last_name
            if last:
                fullname = f"{first} {last}"
            else:
                fullname = first
            username = f"@{a_user.username}" if a_user.username else mention
            userid = a_user.id
            my_first = me.first_name
            my_last = me.last_name
            if my_last:
                my_fullname = f"{my_first} {my_last}"
            else:
                my_fullname = my_first
            my_username = f"@{me.username}" if me.username else my_mention
            file_media = None
            current_saved_welcome_message = None
            if cws and cws.f_mesg_id:
                msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                        ids=int(cws.f_mesg_id))
                file_media = msg_o.media
                current_saved_welcome_message = msg_o.message
            elif cws and cws.reply:
                current_saved_welcome_message = cws.reply
            current_message = await event.reply(
                current_saved_welcome_message.format(mention=mention,
                                                     title=title,
                                                     count=count,
                                                     first=first,
                                                     last=last,
                                                     fullname=fullname,
                                                     username=username,
                                                     userid=userid,
                                                     my_first=my_first,
                                                     my_last=my_last,
                                                     my_fullname=my_fullname,
                                                     my_username=my_username,
                                                     my_mention=my_mention),
                file=file_media)
            update_previous_welcome(event.chat_id, current_message.id)


@bot.on(xubot_cmd(outgoing=True, pattern=r"setwelcome(?: |$)(.*)"))
async def save_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import add_welcome_setting
    except AttributeError:
        return await event.edit("`Running on Non-SQL mode!`")
    msg = await event.get_reply_message()
    string = event.pattern_match.group(1)
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#WELCOME_NOTE \nCHAT ID: {event.chat_id}"
                "\nThe following message is saved as the new welcome note "
                "for the chat, please do NOT delete it !!"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            return await event.edit(
                "`Saving media as part of the welcome note requires the BOTLOG_CHATID to be set.`"
            )
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "`Welcome Berhasil Di {} Di Sini....`"
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        await event.edit(success.format('SIMPAN'))
    else:
        await event.edit(success.format('updated'))


@bot.on(xubot_cmd(outgoing=True, pattern="checkwelcome$"))
async def show_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import get_current_welcome_settings
    except AttributeError:
        return await event.edit("`Running on Non-SQL mode!`")
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        return await event.edit("`Tidak Ada Welcome Yg Di Simpan Di sini..`")
    elif cws and cws.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(cws.f_mesg_id))
        await event.edit(
            "`Hmm, Sepertinya Anda Telah Membuat Welcome Di Sini.`")
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws and cws.reply:
        await event.edit(
            "`Hmm, Sepertinya Anda Telah Membuat Welcome Di Sini.`")
        await event.reply(cws.reply)


@bot.on(xubot_cmd(outgoing=True, pattern="rmwelcome$"))
async def del_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import rm_welcome_setting
    except AttributeError:
        return await event.edit("`Running on Non-SQL mode!`")
    if rm_welcome_setting(event.chat_id) is True:
        await event.edit("`Welcome Berhasil Di Hapus Dari Group Ini.`")
    else:
        await event.edit("`Tidak Ada Welcome Disini, Goblok!! ?`")


CMD_HELP.update({
    "welcome":
    f">`{xcm}setwelcome <welcome message> or reply to a message with .setwelcome`"
    "\nUsage: Saves the message as a welcome note in the chat."
    "\n\nAvailable variables for formatting welcome messages :"
    "\n`{mention}, {title}, {count}, {first}, {last}, {fullname}, "
    "{userid}, {username}, {my_first}, {my_fullname}, {my_last}, "
    "{my_mention}, {my_username}`"
    f"\n\n>`{xcm}checkwelcome`"
    "\nUsage: Check whether you have a welcome note in the chat."
    f"\n\n>`{xcm}rmwelcome`"
    "\nUsage: Deletes the welcome note for the current chat."
})
