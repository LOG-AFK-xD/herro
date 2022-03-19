import random

from pyrogram import filters
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent,
                            Message)

from Hero import SUDOERS, app, random_assistant
from Hero.Database import get_assistant, save_assistant
from Hero.Utilities.assistant import get_assistant_details

__MODULE__ = "Assistant"
__HELP__ = f"""


`/checkassistant`
- Check the Alloted Assistant of your chat


**Note:**
-Only For Sudo User

`/changeassistant` [Ass Number]
- Change The Previous Alloted Assistant Of Your Chat .

`/setassistant` [Only For Sudo Users]
- Set A Assistant Account For Chat. 
"""


ass_num_list = ["1", "2", "3", "4", "5"]


@app.on_message(filters.command(["change", "changeassistant"]) & filters.user(SUDOERS))
async def assis_change(_, message: Message):
    usage = f"**Usage:**\n`/changeassistant` [ASS_NO]\n\nsElect From Them\n{' | '.join(ass_num_list)}"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    num = message.text.split(None, 1)[1].strip()
    if num not in ass_num_list:
        return await message.reply_text(usage)
    ass_num = int(message.text.strip().split()[1])
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        return await message.reply_text(
            "No Pre-Saved Assistant Found ...\n\nYou Can Set Assistant Via/setassistant"
        )
    else:
        ass = _assistant["saveassistant"]
    assis = {
        "saveassistant": ass_num,
    }
    await save_assistant(message.chat.id, "assistant", assis)
    await message.reply_text(
        f"**Changed Assistant**\n\nChanged Assistant Account From **{ass}** To Assistant Number **{ass_num}**"
    )


ass_num_list2 = ["1", "2", "3", "4", "5", "Random"]


@app.on_message(filters.command(["set", "setassistant"]) & filters.user(SUDOERS))
async def assis_change(_, message: Message):
    usage = f"**ᴜsᴀɢᴇ:**\n`/setassistant` [ASS_NO or Random]\n\nSelect From Them\n{' | '.join(ass_num_list2)}\n\nᴜsᴇ 'Random' ᴛᴏ sᴇᴛ ʀᴀɴᴅᴏᴍ ᴀssɪsᴛᴀɴᴛ"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    query = message.text.split(None, 1)[1].strip()
    if query not in ass_num_list2:
        return await message.reply_text(usage)
    if str(query) == "Random":
        ran_ass = random.choice(random_assistant)
    else:
        ran_ass = int(message.text.strip().split()[1])
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        await message.reply_text(
            f"**__Music Bot Assistant Allotted__**\n\nAssistant Number. **{ran_ass}**"
        )
        assis = {
            "saveassistant": ran_ass,
        }
        await save_assistant(message.chat.id, "assistant", assis)
    else:
        ass = _assistant["saveassistant"]
        return await message.reply_text(
            f"Pre-Saved Assistant Number {ass} Found...\n\nYou Can Changed Assistant Via /changeassistant"
        )


@app.on_message(filters.command("checkassistant") & filters.group)
async def check_ass(_, message: Message):
    _assistant = await get_assistant(message.chat.id, "assistant")
    if not _assistant:
        return await message.reply_text(
            "No Pre-Saved Assistant Found...\n\nYou Can Set Assistant Via /play"
        )
    else:
        ass = _assistant["saveassistant"]
        return await message.reply_text(
            f"\n\nNo Pre-Saved Assistant Found {ass} "
        )
