from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import io
from userbot import bot, CMD_HELP
from userbot.events import xubot_cmd
from userbot import CUSTOM_CMD as xcm


@bot.on(xubot_cmd(outgoing=True, pattern="itos$"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("sir this is not a image message reply to image message")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("sir, This is not a image ")
        return
    chat = "@buildstickerbot"
    await event.edit("Membuat Sticker..")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=164977173))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("unblock me (@buildstickerbot) and try again")
            return
        if response.text.startswith("Hi!"):
            await event.edit("Can you kindly disable your forward privacy settings for good?")
        else:
            await event.delete()
            await bot.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, response.message)
            await event.client.delete_message(conv.chat_id, [msg.id, response.id])


@bot.on(xubot_cmd(outgoing=True, pattern="get$"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Balas di Sticker Goblok!!")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("Balas di Sticker Tolol!!")
        return
    chat = "@stickers_to_image_bot"
    await event.edit("Convert to image..")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("unblock me (@stickers_to_image_bot) to work")
            return
        if response.text.startswith("I understand only stickers"):
            await event.edit("Sorry i cant't convert it check wheter is non animated sticker or not")
        else:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            response = await response
            if response.text.startswith("..."):
                response = conv.wait_event(
                    events.NewMessage(
                        incoming=True,
                        from_users=611085086))
                response = await response
                await event.delete()
                await event.client.send_message(event.chat_id, response.message, reply_to=reply_message.id)
                await event.client.delete_messages(conv.chat_id,
                                                   [msg.id, response.id])
            else:
                await event.edit("try again")
        await bot.send_read_acknowledge(conv.chat_id)


@bot.on(xubot_cmd(outgoing=True, pattern="stoi$"))
async def sticker_to_png(sticker):
    if not sticker.is_reply:
        await sticker.edit("`NULL information to feftch...`")
        return False

    img = await sticker.get_reply_message()
    if not img.document:
        await sticker.edit("Ini Bukan sticker Goblok!!!...`")
        return False

    await sticker.edit("`Stiker Berhasil Di Colong!`")
    image = io.BytesIO()
    await sticker.client.download_media(img, image)
    image.name = "sticker.png"
    image.seek(0)
    await sticker.client.send_file(
        sticker.chat_id, image, reply_to=img.id, force_document=True
    )
    await sticker.delete()
    return


CMD_HELP.update(
    {
        "stickerstools": f">`{xcm}itos`"
        "\nUsage: Reply .itos to a sticker or an image to kang it to your userbot no pack "
        f"\n\n>`{xcm}get`"
        "\nUsage: reply to a sticker to get 'PNG' file of sticker."
        f"\n\n>`{xcm}stoi`"
        "\nUsage: reply to a sticker to get 'PNG' file of sticker."})
