import asyncio
import logging
import os
import json
from typing import List, Union

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, BotCommand
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.exceptions import TelegramNetworkError

# КОНФІГУРАЦІЯ
TOKEN = "7286444208:AAEbQB7Lp9RaN46rV_NwHGqxSyMTRM7Nqk4"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot_logger.log", mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# СТАНИ
class BrawlerBuild(StatesGroup):
    name = State()
    select_gadgets = State()
    select_gears = State()

# ФУНКЦІЇ ДАНИХ
def load_brawlers():
    if not os.path.exists('data.json'): return []
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except: return []

def save_brawler(new_data):
    data = load_brawlers()
    data.append(new_data)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# КЛАВІАТУРИ
def get_main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="📋 Список білдів")
    builder.button(text="➕ Додати персонажа")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

# БОТ ТА ДИСПЕТЧЕР
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    try:
        await message.answer(f"Привіт, {html.bold(message.from_user.full_name)}!", reply_markup=get_main_menu())
    except TelegramNetworkError:
        logger.error("Помилка мережі при старті!")

@dp.message(lambda message: message.text == "➕ Додати персонажа")
async def add_start(message: Message, state: FSMContext):
    await message.answer("Введіть ім'я персонажа:")
    await state.set_state(BrawlerBuild.name)

@dp.message(BrawlerBuild.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f"Який гаджет для {message.text}?")
    await state.set_state(BrawlerBuild.select_gadgets)

@dp.message(BrawlerBuild.select_gadgets)
async def process_gadget(message: Message, state: FSMContext):
    user_data = await state.get_data()
    new_build = {
        "name": user_data['name'],
        "gadget": message.text,
        "rare": "Common"
    }
    save_brawler(new_build)
    await state.clear()
    await message.answer(f"✅ Білд для {user_data['name']} збережено!", reply_markup=get_main_menu())

async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="Запуск"),
        BotCommand(command="add_build", description="Додати")
    ])
    # Skip_updates допоможе, якщо бот довго був офлайн
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Бот зупинений")
    except Exception as e:
        logger.critical(f"Критична помилка: {e}")




