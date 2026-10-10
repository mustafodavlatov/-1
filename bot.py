pip install aiogram
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Вставьте сюда токен, полученный от @BotFather
TOKEN = "8846346730:AAGTmfM7OPM0LUowYIicO6rK_GMk6Z25gv4"

bot = Bot(8846346730:AAGTmfM7OPM0LUowYIicO6rK_GMk6Z25gv4)
dp = Dispatcher()

# Ответ на команду /start
@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer("Здравствуйте! Я бот-автоответчик. Чем могу помочь?")

# Автоответчик по ключевым словам или на любые сообщения
@dp.message()
async def auto_reply(message: types.Message):
    text = message.text.lower()

    if "цена" in text or "стоимость" in text:
        await message.answer("Наши тарифы доступны на сайте или по запросу у менеджера.")
    elif "график" in text or "время" in text:
        await message.answer("Мы работаем с понедельника по пятницу с 9:00 до 18:00.")
    else:
        await message.answer("Спасибо за сообщение! Мы ответим вам в ближайшее время.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
