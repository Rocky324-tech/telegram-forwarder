import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

# ================= CONFIG =================

API_ID = 39218730
API_HASH = "97ac27160280bf3ece3c3fb85ae22123"

SESSION_STRING = "BQJWbioAdeOTcPy1ha-lnt_D1QkWJzHMADFHY65HchvZ_ft08GuIVo9FoCYxCCrhCGWjjCfJv_IXr8m5N6LRv1xeWBtLoywM6fmprUBKAzIN4tSeokjWUDlwzI1j8bj-U6sB0WkVxtH1jiWk2W6MqdKwWdrdSCGz0bAqmF2UFm_gdMy8LR-zIqIF7h90ONYPgY-qfBH8zIQVEP_NXv6fLTr03t8QnsBLbEcfoNrgca5mQ0NwGQcmuuOtO0fMC49-dwd9QWKjAKZAGi2W9Dni4hVtR9_edVotfinm0DdJ7mHFPjvmA16xtlafXV1oWvwmnM4pL_NiERBUF-KoQFQayxCWT2t78wAAAAH5OFoHAA"

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
    "ultra_pro",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    workers=100
)

SOURCE_IDS = []
DEST_IDS = []


async def resolve(link):
    try:
        if "+" in link:
            chat = await app.join_chat(link)
        else:
            username = link.split("/")[-1]
            chat = await app.get_chat(username)

        return chat.id

    except Exception as e:

        if "USER_ALREADY_PARTICIPANT" in str(e):
            username = link.split("/")[-1].replace("+", "")
            chat = await app.get_chat(username)
            return chat.id

        logging.error(e)
        return None


async def setup():

    logging.info("Resolving sources...")

    for link in SOURCE_LINKS:
        cid = await resolve(link)
        if cid:
            SOURCE_IDS.append(cid)
            logging.info(f"Source OK: {cid}")

    logging.info("Resolving destinations...")

    for link in DEST_LINKS:
        cid = await resolve(link)
        if cid:
            DEST_IDS.append(cid)
            logging.info(f"Destination OK: {cid}")


@app.on_message(filters.all)
async def forward_handler(client, message):

    if message.chat.id not in SOURCE_IDS:
        return

    logging.info(f"New message from {message.chat.id}")

    for dest in DEST_IDS:

        try:
            await message.copy(dest)

        except FloodWait as e:
            await asyncio.sleep(e.value)

        except Exception as e:
            logging.error(e)


async def main():

    await app.start()

    logging.info("🚀 FORWARDER STARTED")

    await setup()

    logging.info("🔥 RUNNING 24/7")

    await asyncio.Event().wait()


asyncio.run(main())
