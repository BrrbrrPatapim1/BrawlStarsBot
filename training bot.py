import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext # Виправлено: FSMContext замість SSLContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from state_machine import BrawlerBuild, async_log_function_call
from config import TOKEN

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
dp = Dispatcher()

game_genres = ["Brawl stars character guide"]

def create_genre_keyboard():
    builder = InlineKeyboardBuilder()
    for genre in game_genres:
        builder.button(text=genre, callback_data=f"genre_{genre}")
    builder.adjust(1)
    return builder.as_markup()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(
        "Вітаю! Обери жанр гри:",
        reply_markup=create_genre_keyboard()
    )

@dp.message(Command("add_build"))
@async_log_function_call
async def add_build_start(message: Message, state: FSMContext):
    await message.answer("Введіть ім'я персонажа:")
    await state.set_state(BrawlerBuild.name) # Виправлено стан

@dp.message(BrawlerBuild.name)
async def process_character_name(message: Message, state: FSMContext):
    # Виправлено: прибрано await перед message.text
    char_name = message.text 
    await state.update_data(name=char_name) 
    await message.answer(f"Персонаж {char_name} прийнятий. Який гаджет йому підходить?")
    await state.set_state(BrawlerBuild.select_gadgets)

@dp.callback_query()
async def handle_genre(callback: CallbackQuery):
    genre = callback.data.replace("genre_", "")
    await callback.message.answer(f"Ти обрав жанр: {genre}")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Бот зупинений")
    

   