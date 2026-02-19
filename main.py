import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

# ==============================
# YOUR API DETAILS
# ==============================

API_ID = 39218730
API_HASH = "97ac27160280bf3ece3c3fb85ae22123"

SESSION_STRING = "BQJWbioAdeOTcPy1ha-lnt_D1QkWJzHMADFHY65HchvZ_ft08GuIVo9FoCYxCCrhCGWjjCfJv_IXr8m5N6LRv1xeWBtLoywM6fmprUBKAzIN4tSeokjWUDlwzI1j8bj-U6sB0WkVxtH1jiWk2W6MqdKwWdrdSCGz0bAqmF2UFm_gdMy8LR-zIqIF7h90ONYPgY-qfBH8zIQVEP_NXv6fLTr03t8QnsBLbEcfoNrgca5mQ0NwGQcmuuOtO0fMC49-dwd9QWKjAKZAGi2W9Dni4hVtR9_edVotfinm0DdJ7mHFPjvmA16xtlafXV1oWvwmnM4pL_NiERBUF-KoQFQayxCWT2t78wAAAAH5OFoHAA"

# ==============================
# SOURCE AND DESTINATION
# ==============================

SOURCE_CHATS = [
    "livetvo",
    "CKHzywfhEMxiMTdl"
]

DEST_CHATS = [
    "t20bapu",
    "Fan1cricket"
]

# ==============================

app = Client(
    "forwarder",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

resolved_sources = []
resolved_dests = []


@app.on_message(filters.all)
async def forward_handler(client, message):

    if message.chat.id not in resolved_sources:
        return

    for dest in resolved_dests:

        try:
            await message.copy(dest)
            print(f"Forwarded to {dest}")

        except FloodWait as e:
            print(f"FloodWait {e.value}")
            await asyncio.sleep(e.value)

        except Exception as e:
            print(f"Error: {e}")


async def resolve():

    global resolved_sources, resolved_dests

    print("ULTRA PRO AUTO RESOLVE FORWARDER STARTED")

    for chat in SOURCE_CHATS:
        c = await app.get_chat(chat)
        resolved_sources.append(c.id)
        print(f"Source resolved: {chat} -> {c.id}")

    for chat in DEST_CHATS:
        c = await app.get_chat(chat)
        resolved_dests.append(c.id)
        print(f"Dest resolved: {chat} -> {c.id}")


async def main():

    await app.start()

    await resolve()

    print("Forwarder Running 24/7")

    await idle()


from pyrogram import idle

asyncio.run(main())
