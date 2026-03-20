
TOKEN = "7286444208:AAEbQB7Lp9RaN46rV_NwHGqxSyMTRM7Nqk4"
import asyncio
import sys
from aiogram import Bot

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# --------------------------------------------------------


async def test_connection():
    bot = Bot(token=TOKEN)
    try:
        print("Стукаємо до Telegram...")
        me = await bot.get_me()
        print(f"✅ Успіх! З'єднання є. Ім'я вашого бота: {me.first_name}")
    except Exception as e:
        print(f"❌ Помилка підключення: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(test_connection())                                                                                                                                       

