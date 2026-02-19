import asyncio
import logging
from pyrogram import Client, filters, idle
from pyrogram.errors import FloodWait, PeerIdInvalid, RPCError
from pyrogram.raw.functions.channels import JoinChannel

# LOGGING
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# YOUR SESSION STRING
SESSION_STRING = "BQJWbioAdeOTcPy1ha-lnt_D1QkWJzHMADFHY65HchvZ_ft08GuIVo9FoCYxCCrhCGWjjCfJv_IXr8m5N6LRv1xeWBtLoywM6fmprUBKAzIN4tSeokjWUDlwzI1j8bj-U6sB0WkVxtH1jiWk2W6MqdKwWdrdSCGz0bAqmF2UFm_gdMy8LR-zIqIF7h90ONYPgY-qfBH8zIQVEP_NXv6fLTr03t8QnsBLbEcfoNrgca5mQ0NwGQcmuuOtO0fMC49-dwd9QWKjAKZAGi2W9Dni4hVtR9_edVotfinm0DdJ7mHFPjvmA16xtlafXV1oWvwmnM4pL_NiERBUF-KoQFQayxCWT2t78wAAAAH5OFoHAA"

# SOURCE CHATS
SOURCE_CHATS = [
    -1003798031630,
    -1001912679284
]

# DESTINATION CHATS
DESTINATION_CHATS = [
    -1003889857801,
    -1003793224429
]

# CLIENT
app = Client(
    "ultra_pro_forwarder",
    session_string=SESSION_STRING,
    api_id=6,
    api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",
    workers=10
)

# AUTO JOIN FUNCTION
async def auto_join():
    logging.info("Checking chat access...")

    for chat_id in SOURCE_CHATS + DESTINATION_CHATS:
        try:
            await app.get_chat(chat_id)
            logging.info(f"Access OK: {chat_id}")
        except PeerIdInvalid:
            try:
                peer = await app.resolve_peer(chat_id)
                await app.invoke(JoinChannel(channel=peer))
                logging.info(f"Joined: {chat_id}")
            except Exception as e:
                logging.error(f"Join failed {chat_id}: {e}")

# COPY FUNCTION (NO FORWARD TAG)
async def safe_copy(message, dest):
    try:
        await message.copy(dest)
        logging.info(f"Copied to {dest}")

    except FloodWait as e:
        logging.warning(f"FloodWait {e.value}s")
        await asyncio.sleep(e.value)
        await safe_copy(message, dest)

    except RPCError as e:
        logging.error(f"RPCError: {e}")

    except Exception as e:
        logging.error(f"Copy error: {e}")

# MESSAGE HANDLER
@app.on_message(filters.chat(SOURCE_CHATS))
async def handler(client, message):

    # skip service messages
    if message.service:
        return

    tasks = []

    for dest in DESTINATION_CHATS:
        tasks.append(safe_copy(message, dest))

    await asyncio.gather(*tasks)

# MAIN START
async def main():

    while True:

        try:
            await app.start()

            logging.info("🚀 ULTRA PRO FORWARDER STARTED")

            await auto_join()

            await idle()

        except Exception as e:
            logging.error(f"Crash detected: {e}")
            logging.info("Restarting in 5 seconds...")
            await asyncio.sleep(5)

        finally:
            await app.stop()

# RUN
asyncio.run(main())
