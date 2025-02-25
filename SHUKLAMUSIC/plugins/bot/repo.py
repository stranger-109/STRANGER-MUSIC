from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC import app
from config import BOT_USERNAME
from SHUKLAMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ωεℓ¢σмє тσ ѕнυвн мσνιєѕ ✪
 
 ➲ ɢᴇᴛ ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴠɪᴇ ғᴏʀ ғʀᴇᴇ. 
 
 ➲ ᴀʟʟ ɴᴇᴡ ᴍᴏᴠɪᴇs ᴀʀᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ʜᴇʀᴇ 
 
 ➲ ɪғ ᴛʜᴇ ᴍᴏᴠɪᴇ ᴡᴀs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴀᴛ ᴛʜᴀᴛ ᴛɪᴍᴇ ʏᴏᴜ 
 ᴄᴀɴ ʀᴇǫᴜᴇsᴛ ɪᴛ ᴀᴛ ➲ @SUBMISSIONS1227_bot
 
  ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("movie"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/Mrshubh_1227"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/Demonxcoder"),
          ],
               [
                InlineKeyboardButton("𝗚𝗘𝗧 𝗔𝗡𝗬 𝗠𝗢𝗩𝗜𝗘", url="https://t.me/MoviesWDs_bot"),

        ]]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://graph.org/file/db0fbc02a08c2a28349f1-3671ff24b68aa73e82.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


# --------------


@app.on_message(filters.command("movie", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/Shubhxspam/STRANGER-MUSIC/contributors")

    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[Movies](https://t.me/MoviesWDs_bot) | [MOVIE](https://t.me/MoviesWDs_bot)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
