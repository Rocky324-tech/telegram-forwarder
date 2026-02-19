import asyncio
from pyrogram import Client, filters
from pyrogram.errors import RPCError

api_id = 39218730
api_hash = "97ac27160280bf3ece3c3fb85ae22123"

session_string = "PASTE_YOUR_STRING_HERE"

sources = [
    -1003798031630,
    -1001912679284
]

destinations = [
    -1003793224429,
    -1003889857801
]

app = Client(
    "forwarder",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string
)

@app.on_message(filters.chat(sources))
async def forward_handler(client, message):
    print(f"\nMESSAGE DETECTED: {message.id}")
    print(f"FROM CHAT: {message.chat.id}")

    for dest in destinations:
        try:
            await message.copy(dest)
            print(f"SUCCESS → copied to {dest}")
        except RPCError as e:
            print(f"ERROR → {dest} → {e}")

print("DEBUG FORWARDER STARTED")

app.run()
