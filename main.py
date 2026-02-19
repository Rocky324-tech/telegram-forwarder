import asyncio
from pyrogram import Client, filters, idle

api_id = 39218730
api_hash = "97ac27160280bf3ece3c3fb85ae22123"

SESSION = "BQJWbioAGnVxisRP9gzo4pyJCz1eHrviCVzATI3ogtiyQLT_1jrzCSlJcmT3qOQEyDef1W9btyk3XANpMXDDmiG0Kx5-KUGWmMr0uv6T_fRA8h_KLb1o2itfDp53QhTZtCjDHzxuJXa6XXWqA4lDFqc0RM6khxw9WWILePiduv9jd0qDK2TByN1xUiDamGDsBfVF9u1xHKrJDnIVSi-fahcpp7FVLDq-KZEfrc7wpt23_Zx9j9dKr2kGdwacyVO6oSUxCt9fjbAkMPPVJ4aXBUEerPw-2Mu50eerD1bvvR_ulqrVwYMZh_FF5BT7xn3cBn2JERqeYCiwYIN4q-idGeJawhTyPAAAAAH5OFoHAA"

SOURCE = [
    -1003798031630,
    -1001912679284
]

DESTINATION = -1003889857801

app = Client(
    SESSION,
    api_id=api_id,
    api_hash=api_hash
)

@app.on_message(filters.chat(SOURCE))
async def forward(client, message):
    await message.copy(DESTINATION)

async def main():
    await app.start()
    print("Forwarder running...")
    await idle()

asyncio.run(main())
