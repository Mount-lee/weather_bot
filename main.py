import math
import datetime
import requests
import asyncio
from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command

bot = Bot(token="7227056260:AAGPWOrcZwOsYUDICEeffENCxKqHt93PaQU")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет"
                         "\nВведите город:")


@dp.message()
async def get_data(message: types.Message):
    answer = message.text
    try:
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={answer}&lang=ru&appid=395048665aa3c1c24f1b0d69eb834246")
        data = res.json()
        city = data["name"]
        temp = data["main"]["temp"]
        pressure = data["main"]["pressure"]

    except:
        await message.reply("Проверьте название города!")
    await message.answer(f"{datetime.datetime.now().strftime('%Y-%m-%d / %H:%M')}"
                         f"\nВ городе {city} температура {math.ceil(temp-273)} °C"
                         f"\nДавление: {math.ceil(pressure/1.333)} мм.рт.ст.")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())