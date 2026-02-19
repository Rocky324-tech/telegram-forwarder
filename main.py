import asyncio
from pyrogram import Client, filters
from pyrogram.errors import RPCError

api_id = 39218730
api_hash = "97ac27160280bf3ece3c3fb85ae22123"

session_string = "BQJWbioAdeOTcPy1ha-lnt_D1QkWJzHMADFHY65HchvZ_ft08GuIVo9FoCYxCCrhCGWjjCfJv_IXr8m5N6LRv1xeWBtLoywM6fmprUBKAzIN4tSeokjWUDlwzI1j8bj-U6sB0WkVxtH1jiWk2W6MqdKwWdrdSCGz0bAqmF2UFm_gdMy8LR-zIqIF7h90ONYPgY-qfBH8zIQVEP_NXv6fLTr03t8QnsBLbEcfoNrgca5mQ0NwGQcmuuOtO0fMC49-dwd9QWKjAKZAGi2W9Dni4hVtR9_edVotfinm0DdJ7mHFPjvmA16xtlafXV1oWvwmnM4pL_NiERBUF-KoQFQayxCWT2t78wAAAAH5OFoHAA"

# sources (ID)
source_ids = [
    -1003798031630,
    -1001912679284
]

# destinations (username)
destination_usernames = [
    "t20bapu",
    "Fan1cricket"
]

app = Client(
    "forwarder",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string
)

destination_ids = []

async def resolve_destinations():
    global destination_ids
    for username in destination_usernames:
        try:
            chat = await app.get_chat(username)
            destination_ids.append(chat.id)
            print(f"Resolved {username} → {chat.id}")
        except Exception as e:
            print(f"Resolve failed {username}: {e}")

@app.on_message(filters.chat(source_ids))
async def handler(client, message):
    print("Message detected")
    for dest in destination_ids:
        try:
            await message.copy(dest)
            print(f"Copied to {dest}")
        except RPCError as e:
            print(e)

async def main():
    await app.start()
    print("ULTRA PRO AUTO RESOLVE FORWARDER STARTED")
    await resolve_destinations()
    await asyncio.Event().wait()

asyncio.run(main())
