# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import bot, CMD_HELP
from userbot.events import xubot_cmd
from userbot import CUSTOM_CMD as xcm

modules = CMD_HELP


@bot.on(xubot_cmd(outgoing=True, pattern="help(?: |$)(.*)"))
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Module Salah Goblokkkk!!**")
            await asyncio.sleep(18)
            await event.delete()
    else:
        await event.edit(f"**╭━━━━━━━━━━━━━━━━━━━╮**\
            \n│   Help for ☠️ X-USERBOT ☠️\
            \n╰━━━━━━━━━━━━━━━━━━━╯ \
            \n╭━━━━━━━━━━━━━━━━━━━╮\
            \n│  Untuk melihat lengkap CMD\
            \n│  Contoh: {xcm}help <nama module>\
            \n│  Modules Aktif: {len(modules)}\
           \n╰━━━━━━━━━━━━━━━━━━━╯")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t• "
        await event.reply("╾───────────────────╼\n" f"•{string}•"
                          "\n╾───────────────────╼")
        await asyncio.sleep(100)
        await event.delete()
