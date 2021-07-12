# Thank you to @Badboyanim for this awesome module
#

import os

import moviepy.editor as m

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.getaudio(?: |$)(.*)")
async def daudtoid(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("audio" in ureply.document.mime_type)):
        await event.edit("`Reply To Audio Only..`")
        return
    await event.edit("`processing...`")
    d = os.path.join("resources/extras", "ul.mp3")
    await event.edit("`Downloading... Large Files Takes Time..`")
    await event.client.download_media(ureply, d)
    await event.edit("`Done.. Now reply to video In which u want to add that Audio`")


@register(outgoing=True, pattern="^.addaudio(?: |$)(.*)")
async def adaudroid(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("video" in ureply.document.mime_type)):
        await event.edit("`Reply To Gif/Video In which u want to add audio.`")
        return
    await event.edit("`processing...`")
    ultt = await ureply.download_media()
    ls = os.listdir("resources/extras")
    z = "ul.mp3"
    x = "resources/extras/ul.mp3"
    if z not in ls:
        await event.edit("`First reply an audio with .aw`")
        return
    video = m.VideoFileClip(ultt)
    audio = m.AudioFileClip(x)
    out = video.set_audio(audio)
    out.write_videofile("ok.mp4", fps=30)
    await event.client.send_file(
        event.chat_id,
        file="ok.mp4",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    os.remove("ok.mp4")
    os.remove(x)
    os.remove(ultt)
    await event.delete()


CMD_HELP.update(
    {
        "audio": "📚 **Cmd** : `.getaudio`\
         \n📄 **Descriptions** : Download Audio To put in ur Desired Video/Gif..\
         \n📚 **Cmd** : `.addaudio`\
         \n📄 **Descriptions : It will put the above audio to the replied video/gif.."
    }
)
