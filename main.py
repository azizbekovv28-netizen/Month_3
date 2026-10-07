import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}, я твой первый бот"
    )

    print(f"Пользователь{message.from_user.full_name} под ником {message.from_user.username} отправил команду /start")

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        f"/start - приветствие\n"
        "/help - список команд"
    )

@dp.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(
        "Я новый Telegram-бот\n"
        "Я умею отвечать на команды, реагировать на определённые слова "
        "и повторять твои сообщения "
    )

@dp.message(F.text.lower() == "группа")
async def cmd_group(message: Message):
    await message.answer(f"Твоя группа  70 - 1")

@dp.message(F.text.lower() == "пока")
async def cmd_bye(message: Message):
    await message.answer(f"Пока! Хорошего дня!")


@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
