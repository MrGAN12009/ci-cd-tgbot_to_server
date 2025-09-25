import asyncio
from aiogram import Bot, Dispatcher, types

#123
TOKEN = "8056530991:AAEgU6VIE6_SDFftjUXey_80AmZj7ANYpyI"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
