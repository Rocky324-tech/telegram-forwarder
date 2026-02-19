import os
from pyrogram import Client, filters
from pyrogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHAT = int(os.getenv("SOURCE_CHAT"))
DEST_CHATS = os.getenv("DEST_CHATS").split(",")

app = Client(
    "forwarder_bot",
    bot_token=BOT_TOKEN,
    api_id=12345,
    api_hash="0123456789abcdef0123456789abcdef"
)

@app.on_message(filters.chat(SOURCE_CHAT))
async def forward_messages(client, message: Message):
    for chat_id in DEST_CHATS:
        try:
            await message.forward(int(chat_id))
            print(f"Forwarded to {chat_id}")
        except Exception as e:
            print(f"Error: {e}")

print("Bot started...")
app.run()
