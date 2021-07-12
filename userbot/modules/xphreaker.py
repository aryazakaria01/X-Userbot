# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Created By @ximfine

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
import asyncio
from userbot.events import xubot_cmd
from userbot import CUSTOM_CMD as xcm


@bot.on(xubot_cmd(outgoing=True, pattern="gen(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan bin yang mau di generate!..__")
    await event.edit(f"```Generated CC {query}..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/gen {query}")
            await asyncio.sleep(4)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Gagal generate {query}!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@bot.on(xubot_cmd(outgoing=True, pattern="chk(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan cc yang mau di check!..__")
    await event.edit("```Checking CC Number..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/ss {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Gagal Mengecek {query}!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@bot.on(xubot_cmd(outgoing=True, pattern="bin(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan BIN yang mau di check!..__")
    await event.edit(f"```Checking BIN {query}```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/bin {query}")
            await asyncio.sleep(5)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Bin {query} Invalid!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@bot.on(xubot_cmd(outgoing=True, pattern="skey(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan SK-KEY yang mau di check!..__")
    await event.edit(f"```Checking SK KEY {query}```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/bin {query}")
            await asyncio.sleep(5)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit("SK KEY Invalid!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@bot.on(xubot_cmd(outgoing=True, pattern="nmap(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan domain yang mau di check!..__")
    await event.edit(f"```Getting info {query}..```")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/nmap {query}")
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @scriptkiddies_bot atau chat dulu")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@bot.on(xubot_cmd(outgoing=True, pattern="subd(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan domain yang mau di generate!..__")
    await event.edit(f"```Generated subdomain {query}..```")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/subdomain {query}")
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @scriptkiddies_bot atau chat dulu")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@bot.on(xubot_cmd(outgoing=True, pattern="cekhttp(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan domain yang mau di check!..__")
    await event.edit(f"```Checking Respond {query}..```")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/httpheader {query}")
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @scriptkiddies_bot atau chat dulu")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


CMD_HELP.update({
    "xphreaker":
    f"**HELP FOR XPHREAKER**\
\n╭━━━━━━━━━━━━━━━━━━━╮\
\n  `{xcm}gen <bin>`\
\n   Usage: to generate cc with bin.\
\n\n  `{xcm}chk <cc>`\
\n   Usage: to check respond cc.\
\n\n  `{xcm}bin <bin number>`\
\n   Usage: to cek bin information.\
\n\n  `{xcm}skey <SK-KEY>`\
\n   Usage: to check skkey respond.\
\n\n  `{xcm}nmap <domain hosts>`\
\n   Usage: to get info bug/host.\
\n\n  `{xcm}subd <domain hosts>`\
\n   Usage: to get subdomain bug/host.\
\n\n  `{xcm}cekhttp <domain hosts>`\
\n   Usage: to cek respons bug/host.\
\n╰━━━━━━━━━━━━━━━━━━━╯"
})
