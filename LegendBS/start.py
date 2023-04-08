from pyrogram.types import InlineKeyboardButton

async def start_cmd(Legend):
    x = await Legend.get_me()
    START_OP = [
        [
            InlineKeyboardButton(
                text="🥀 Developer 🥀", url=f"https://t.me/kannadigaxd"
            ),
            InlineKeyboardButton(
                text="✨ Support ✨", url=f"https://t.me/kannada_chatbox"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🧸 Add me in your group 🧸",
                url=f"https://t.me/{x.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❄️ Source Code ❄️", url=f"https://t.me/lovee_and_lustt"
            ),
            InlineKeyboardButton(
                text="☁️ Updates ☁️", url=f"https://t.me/do_jism_ek_jaan_op"
            ),
        ],
    ]
    return START_OP
