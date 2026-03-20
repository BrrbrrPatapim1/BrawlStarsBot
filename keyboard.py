import logging
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

# Виправлено: видалено "from os import name", використовуємо __name__ для логера
logger = logging.getLogger(__name__)

# Основне меню (Reply Keyboard)
def get_main_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    # Додаємо кнопки для основних команд
    builder.button(text=" Список білдів")
    builder.button(text=" Додати персонажа")
    builder.button(text=" Допомога")
    builder.adjust(2) # Кнопки по 2 у ряд
    return builder.as_markup(resize_keyboard=True)

# Вибір рідкісності (Inline Keyboard)
def get_rarity_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    rarities = ["Rare", "Super Rare", "Epic", "Mythic", "Legendary","Ultra Legendary"]
    
    for rare in rarities:
        builder.button(text=rare, callback_data=f"rare_{rare.lower()}")
    
    builder.adjust(2)
    return builder.as_markup()

# Вибір жанру (перенесено з твого списку)
def get_genre_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Brawl Stars Guide", callback_data="genre_brawl_stars")
    return builder.as_markup()
    