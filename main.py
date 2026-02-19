import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import logging

# ================= CONFIG =================

API_ID = 39218730
API_HASH = "97ac27160280bf3ece3c3fb85ae22123"

SESSION = "BQJWbioAdeOTcPy1ha-lnt_D1QkWJzHMADFHY65HchvZ_ft08GuIVo9FoCYxCCrhCGWjjCfJv_IXr8m5N6LRv1xeWBtLoywM6fmprUBKAzIN4tSeokjWUDlwzI1j8bj-U6sB0WkVxtH1jiWk2W6MqdKwWdrdSCGz0bAqmF2UFm_gdMy8LR-zIqIF7h90ONYPgY-qfBH8zIQVEP_NXv6fLTr03t8QnsBLbEcfoNrgca5mQ0NwGQcmuuOtO0fMC49-dwd9QWKjAKZAGi2W9Dni4hVtR9_edVotfinm0DdJ7mHFPjvmA16xtlafXV1oWvwmnM4pL_NiERBUF-KoQFQayxCWT2t78wAAAAH5OFoHAA"

SOURCE_LINKS = [
    "https://t.me/+CKHzywfhEMxiMTdl",
    "https://t.me/livetvo"
]

DEST_LINKS = [
    "https://t.me/t20bapu",
    "https://t.me/Fan1cricket"
]

# ==========================================

logging.basicConfig(level=logging.INFO)

app = Client(
    "forwarder",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
    workers=100
)

source_ids = []
dest_ids = []


async def resolve_chat(link):
    try:
        if "+" in link:
            chat = await app.join_chat(link)
        else:
            username = link.split("/")[-1]
            chat = await app.get_chat(username)
        return chat.id
    except Exception as e:
        logging.error(f"Resolve error {link}: {e}")
        return None


async def init_chats():
    global source_ids, dest_ids

    logging.info("Resolving sources...")
    for link in SOURCE_LINKS:
        cid = await resolve_chat(link)
        if cid:
            source_ids.append(cid)
            logging.info(f"Source OK: {cid}")

    logging.info("Resolving destinations...")
    for link in DEST_LINKS:
        cid = await resolve_chat(link)
        if cid:
            dest_ids.append(cid)
            logging.info(f"Destination OK: {cid}")


@app.on_message(filters.all)
async def ultra_forward(client, message):

    if message.chat.id not in source_ids:
        return

    for dest in dest_ids:
        try:
            await message.copy(dest)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as e:
            logging.error(f"Send error: {e}")


async def main():

    await app.start()

    logging.info("🚀 ULTRA PRO FORWARDER STARTED")

    await init_chats()

    logging.info("✅ READY AND RUNNING 24/7")

    await asyncio.Event().wait()


asyncio.run(main())
