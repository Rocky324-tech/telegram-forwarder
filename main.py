from pyrogram import Client, filters
import os

SESSION = os.environ.get("SESSION")

SOURCE_CHAT = -1003798031630  # your source channel

DESTINATION_CHATS = [
    "t20bapu",
    "Fan1cricket"
]

app = Client(
    "forwarder",
    session_string=SESSION,
    api_id=39218730,
    api_hash="97ac27160280bf3ece3c3fb85ae22123"
)

@app.on_message(filters.chat(SOURCE_CHAT))
async def forward(client, message):
    for dest in DESTINATION_CHATS:
        try:
            await message.forward(dest)
            print(f"Forwarded to {dest}")
        except Exception as e:
            print(f"Error forwarding to {dest}: {e}")

print("Bot started...")
app.run()
