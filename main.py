import asyncio
from pyrogram import Client, filters
from pyrogram.errors import RPCError

api_id = 39218730
api_hash = "97ac27160280bf3ece3c3fb85ae22123"

session_string = "BQJWbioAdeOTcPy1ha-lnt_D1QkWJzHMADFHY65HchvZ_ft08GuIVo9FoCYxCCrhCGWjjCfJv_IXr8m5N6LRv1xeWBtLoywM6fmprUBKAzIN4tSeokjWUDlwzI1j8bj-U6sB0WkVxtH1jiWk2W6MqdKwWdrdSCGz0bAqmF2UFm_gdMy8LR-zIqIF7h90ONYPgY-qfBH8zIQVEP_NXv6fLTr03t8QnsBLbEcfoNrgca5mQ0NwGQcmuuOtO0fMC49-dwd9QWKjAKZAGi2W9Dni4hVtR9_edVotfinm0DdJ7mHFPjvmA16xtlafXV1oWvwmnM4pL_NiERBUF-KoQFQayxCWT2t78wAAAAH5OFoHAA"

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
    print(f"Message detected: {message.id}")
    for dest in destinations:
        try:
            await message.copy(dest)
            print(f"Copied to {dest}")
        except RPCError as e:
            print(f"Error: {e}")

print("ULTRA PRO FORWARDER STARTED")

app.run()
