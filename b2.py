import urllib.request

print("--- Починаємо перевірку мережі ---")

# Тест 1: Чи пускає Python взагалі в інтернет?
try:
    print("1. Перевіряємо Google...")
    urllib.request.urlopen("https://www.google.com", timeout=5)
    print("✅ Google працює! Python має доступ до інтернету.")
except Exception as e:
    print(f"❌ Google недоступний: {e}")

# Тест 2: Чи пускає саме до Telegram?
try:
    print("2. Перевіряємо Telegram...")
    urllib.request.urlopen("https://api.telegram.org", timeout=5)
    print("✅ Telegram працює! Сервери доступні.")
except Exception as e:
    print(f"❌ Telegram недоступний: {e}")

print("--- Перевірка завершена ---")