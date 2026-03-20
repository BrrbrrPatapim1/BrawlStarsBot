import logging 

logger = logging.getLogger(__name__)
from aiogram.fsm.state import State, StatesGroup


class BrawlerBuild(StatesGroup):
    # select_day = State()
    select_gadgets = State()  # Етап 1: Чекаємо назву предмету
    select_gears = State()      # Етап 2: Чекаємо текст завдання
    select_starpowers = State()
    select_characters = State()
    select_rare = State()
    # /search
def async_log_function_call(func):
   """Декоратор для логування викликів асинхронних функцій"""

   async def wrapper(*args, **kwargs):

       logger = logging.getLogger(__name__)
       msg = f"Відбувся виклик функції '{func.__name__}'"
       logger.info(msg=msg)
       return await func(*args, **kwargs)

   return wrapper
