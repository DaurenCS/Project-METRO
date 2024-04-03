import asyncio
import logging
import sys
from aiogram.filters import Command
from os import getenv
from database import *
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from keyboards import make_row_keyboard, start_text
from aiogram import Router, F
import aiohttp

TOKEN = "6471247671:AAGAFa1jDG7H7wXFZ0TqYQje_b8XJvpI12U"

dp = Dispatcher()



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!")
    await message.answer("Какая станция вам нужна?", reply_markup=make_row_keyboard(get_all_stations()))

@dp.message(F.text, Command("exit"))
async def exit_command(message: types.Message):
    await message.answer("До новых встреч !"+ start_text(), reply_markup=types.ReplyKeyboardRemove())
   

@dp.message(F.text)
async def echo_handler(message: types.Message) -> None:
    try:
        if message.text in get_all_stations():

            answer = filter_schedule_by_station(message.text)
            await message.answer(str(answer))
        else:
             await message.answer("Извините. Какая станция вам нужна?", reply_markup=make_row_keyboard(get_all_stations()))
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())