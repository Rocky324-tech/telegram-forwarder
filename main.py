import asyncio
from pyrogram import Client, filters, idle

api_id = 39218730
api_hash = "97ac27160280bf3ece3c3fb85ae22123"

session_string = "BQJWbioAGnVxisRP9gzo4pyJCz1eHrviCVzATI3ogtiyQLT_1jrzCSlJcmT3qOQEyDef1W9btyk3XANpMXDDmiG0Kx5-KUGWmMr0uv6T_fRA8h_KLb1o2itfDp53QhTZtCjDHzxuJXa6XXWqA4lDFqc0RM6khxw9WWILePiduv9jd0qDK2TByN1xUiDamGDsBfVF9u1xHKrJDnIVSi-fahcpp7FVLDq-KZEfrc7wpt23_Zx9j9dKr2kGdwacyVO6oSUxCt9fjbAkMPPVJ4aXBUEerPw-2Mu50eerD1bvvR_ulqrVwYMZh_FF5BT7xn3cBn2JERqeYCiwYIN4q-idGeJawhTyPAAAAAH5OFoHAA"

SOURCE_CHANNELS = [
    -1001912679284,
    -1003798031630
]

DESTINATION_CHANNEL = -1003889857801

app = Client(
    "forwarder",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string,
    workers=200,
    sleep_threshold=0
)

@app.on_message(filters.chat(SOURCE_CHANNELS))
async def forward_handler(client, message):
    try:
        await message.copy(chat_id=DESTINATION_CHANNEL)
        print("Forwarded")
    except Exception as e:
        print(e)

async def main():
    await app.start()
    print("🚀 Forwarder running 24/7 🚀")
    await idle()

asyncio.run(main())
