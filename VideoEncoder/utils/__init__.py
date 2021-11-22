from pyrogram import filters
from pyrogram.errors import RPCError
from . import ffmpeg
from . import progress
from . import tasks
from .. import app as a

sauce = '''<b>VideoEncoder - a telegram bot for compressing/encoding videos in h264 format.
Copyright (c) 2021 WeebTime/VideoEncoder</b>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see .'''

@a.on_message(filters.command('so' 'ur' 'ce'))
async def g_s(_, message):
    try:
        await message.reply_text(sauce)
    except RPCError:
        pass