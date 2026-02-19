import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import os

# ================= CONFIG =================

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")

# AUTO RESOLVE LINKS
SOURCE_CHATS = [
    "livetvo",
    "-1001912679284"
]

DEST_CHATS = [
    "t20bapu",
    "Fan1cricket"
]

# =========================================

app = Client(
    "forwarder",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)


# AUTO RESOLVE FUNCTION
async def resolve(chat):
    try:
        if "t.me/" in chat:
            chat = chat.split("/")[-1]

        entity = await app.get_chat(chat)
        print(f"Resolved: {entity.title}")
        return entity.id

    except Exception as e:
        print(f"Resolve failed {chat}: {e}")
        return None


@app.on_message(filters.all)
async def forward_handler(client, message):

    try:

        if message.chat.username not in SOURCE_CHATS and str(message.chat.id) not in SOURCE_CHATS:
            return

        for dest in DEST_CHATS:

            try:
                await message.copy(dest)
                print(f"Copied to {dest}")

            except FloodWait as e:
                await asyncio.sleep(e.value)
                await message.copy(dest)

            except Exception as err:
                print(f"Error sending to {dest}: {err}")

    except Exception as e:
        print(e)


async def main():

    print("Starting ULTRA PRO Forwarder...")

    await app.start()

    print("Bot Started Successfully")

    await idle()


from pyrogram import idle

app.run(main())
