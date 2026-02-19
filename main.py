import asyncio
from pyrogram import Client, filters

# API details
api_id = 39218730
api_hash = "97ac27160280bf3ece3c3fb85ae22123"

# Session string
session_string = "BQJWbioAdeOTcPy1ha-lnt_D1QkWJzHMADFHY65HchvZ_ft08GuIVo9FoCYxCCrhCGWjjCfJv_IXr8m5N6LRv1xeWBtLoywM6fmprUBKAzIN4tSeokjWUDlwzI1j8bj-U6sB0WkVxtH1jiWk2W6MqdKwWdrdSCGz0bAqmF2UFm_gdMy8LR-zIqIF7h90ONYPgY-qfBH8zIQVEP_NXv6fLTr03t8QnsBLbEcfoNrgca5mQ0NwGQcmuuOtO0fMC49-dwd9QWKjAKZAGi2W9Dni4hVtR9_edVotfinm0DdJ7mHFPjvmA16xtlafXV1oWvwmnM4pL_NiERBUF-KoQFQayxCWT2t78wAAAAH5OFoHAA"

# Multiple sources
SOURCE_CHATS = [
    -1003798031630,
    -1001912679284
]

# Multiple destinations
DESTINATION_CHATS = [
    -1003889857801,
    -1003793224429
]

# Create client
app = Client(
    "forwarder",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string
)

# Turbo forward function
@app.on_message(filters.chat(SOURCE_CHATS))
async def forward_messages(client, message):
    for dest in DESTINATION_CHATS:
        try:
            await message.copy(dest)   # copy = no forward tag
            print(f"Forwarded to {dest}")
        except Exception as e:
            print(f"Error sending to {dest}: {e}")

# Run forever
print("Turbo Forwarder Started Successfully!")
app.run()
