import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

# ========= YOUR CONFIG =========

API_ID = 39218730
API_HASH = "97ac27160280bf3ece3c3fb85ae22123"

SESSION_STRING = "BQJWbioAdeOTcPy1ha-lnt_D1QkWJzHMADFHY65HchvZ_ft08GuIVo9FoCYxCCrhCGWjjCfJv_IXr8m5N6LRv1xeWBtLoywM6fmprUBKAzIN4tSeokjWUDlwzI1j8bj-U6sB0WkVxtH1jiWk2W6MqdKwWdrdSCGz0bAqmF2UFm_gdMy8LR-zIqIF7h90ONYPgY-qfBH8zIQVEP_NXv6fLTr03t8QnsBLbEcfoNrgca5mQ0NwGQcmuuOtO0fMC49-dwd9QWKjAKZAGi2W9Dni4hVtR9_edVotfinm0DdJ7mHFPjvmA16xtlafXV1oWvwmnM4pL_NiERBUF-KoQFQayxCWT2t78wAAAAH5OFoHAA"

SOURCE_IDS = [
    -1003798031630
]

DEST_IDS = [
    -1003889857801
]

# ===============================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

app = Client(
    "ultra_pro_forwarder",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    workers=200
)


@app.on_message(filters.chat(SOURCE_IDS))
async def forward(client, message):

    logging.info(f"Message detected: {message.id}")

    for dest in DEST_IDS:

        try:

            await message.copy(dest)

            logging.info(f"Copied to {dest}")

        except FloodWait as e:

            logging.warning(f"FloodWait {e.value}")
            await asyncio.sleep(e.value)

        except Exception as err:

            logging.error(f"Error: {err}")


async def main():

    await app.start()

    logging.info("🚀 ULTRA PRO FORWARDER STARTED")
    logging.info(f"Listening: {SOURCE_IDS}")
    logging.info(f"Sending to: {DEST_IDS}")

    await asyncio.Event().wait()


asyncio.run(main())
