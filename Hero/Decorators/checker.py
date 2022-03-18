from Hero import BOT_USERNAME, LOG_GROUP_ID, app
from Hero.Database import blacklisted_chats, is_gbanned_user, is_on_off


def checker(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "You're an __Anonymous Admin__ In This Chat Group...\nRevert Back to User account from Admin Rights..."
            )
        blacklisted_chats_list = await blacklisted_chats()
        if message.chat.id in blacklisted_chats_list:
            await message.reply_text(
                f"**Blacklisted Chat**\n\nYour Chat has been Blacklisted by Sudo User Ask Any __SUDO USER__ To Whitelist...\nCheck Sudo Userlist [From Here](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
            return await app.leave_chat(message.chat.id)
        if await is_on_off(1):
            if int(message.chat.id) != int(LOG_GROUP_ID):
                return await message.reply_text(
                    f"Bot Is Under Maintenance Sorry For The Inconvenience"
                )
        if await is_gbanned_user(message.from_user.id):
            return await message.reply_text(
                f"**Gbanned User**\n\nYou're Gbanned From using bot ask any __SUDO USER__ To Ungban...\nCheck Sudo User list [From Here](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
        return await mystic(_, message)

    return wrapper


def checkerCB(mystic):
    async def wrapper(_, CallbackQuery):
        blacklisted_chats_list = await blacklisted_chats()
        if CallbackQuery.message.chat.id in blacklisted_chats_list:
            return await CallbackQuery.answer(
                "Blacklisted Chat", show_alert=True
            )
        if await is_on_off(1):
            if int(CallbackQuery.message.chat.id) != int(LOG_GROUP_ID):
                return await CallbackQuery.answer(
                    "Bot Is Under Maintainec Sorry For The Convenience...",
                    show_alert=True,
                )
        if await is_gbanned_user(CallbackQuery.from_user.id):
            return await CallbackQuery.answer(
                "ʏᴏᴜ'ʀᴇ ɢʙᴀɴɴᴇᴅ", show_alert=True
            )
        return await mystic(_, CallbackQuery)

    return wrapper
