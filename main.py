import os
from pyrogram import Client, filters
from pyrogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHAT = int(os.getenv("SOURCE_CHAT"))
DEST_CHATS = os.getenv("DEST_CHATS").split(",")

app = Client(
    "forwarder_bot",
    bot_token=BOT_TOKEN,
    api_id=39218730,
    api_hash="97ac27160280bf3ece3c3fb85ae22123"
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
