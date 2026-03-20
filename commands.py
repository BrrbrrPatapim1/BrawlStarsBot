from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand

# Фільтри для хендлерів
START_COMMAND = Command('start')
BUILD_COMMAND = Command('builds') 
BUILDCHARACTER_COMMAND = Command('characterbuild')

# Об'єкти для меню кнопок (Bot Menu)
# Виправлено: опис зроблено чіткішим
COMMANDS_LIST = [
    BotCommand(command='start', description="Запустити бота"),
    BotCommand(command='builds', description="Список усіх білдів"),
    BotCommand(command='characterbuild', description="Створити новий білд")
]
