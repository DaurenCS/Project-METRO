from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from database import *
from aiogram import Bot, Dispatcher, Router, types


def make_row_keyboard(list):
    builder = ReplyKeyboardBuilder()
    for station in list:
        builder.add(types.KeyboardButton(text = station))
    builder.adjust(3)   
    keyboard = builder.as_markup(resize_keyboard=True)
    
    return keyboard

def start_text():
    commands = ['/start', '/exit']
    commands_text = "\n".join(commands)
    welcome_message = f" Here are the available commands:\n{commands_text}\nClick the 'Start' button to begin."
    return welcome_message