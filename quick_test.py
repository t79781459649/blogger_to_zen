# quick_test.py
# Ваш тестовый скрипт с РУЧНОЙ проверкой
import telebot
import time

TOKEN = "8099475704:AAEtCKPDVy1ViVD20UzLc8AX01H2bjm8n-A"
CHANNEL = "@anna_roses_crimea"

bot = telebot.TeleBot(TOKEN)

print("=" * 60)
print("ТЕСТ 1: Проверка отправки в Telegram")
print("=" * 60)

# ТЕКСТ БЕЗ ссылок и сложностей
test_text = """[ТЕСТ_1] Наблюдение за розой

Первые заметки о росте растения.

#тест #растение #наблюдение"""

try:
    print("🔄 Отправляю тестовое сообщение...")
    print(f"Текст: {test_text[:50]}...")
    
    # Отправляем
    message = bot.send_message(CHANNEL, test_text)
    
    print(f"✅ Сообщение отправлено!")
    print(f"📱 ID сообщения: {message.message_id}")
    print(f"💬 Текст отправлен в: {CHANNEL}")
    
    print("\n" + "=" * 60)
    print("👤 ВАШИ ДЕЙСТВИЯ СЕЙЧАС:")
    print("1. Откройте Telegram, найдите свой канал")
    print("2. Убедитесь, что пост появился")
    print("3. ВРУЧНУЮ нажмите 'Поделиться' → 'Дзен'")
    print("4. Проверьте, что пост появился в Дзен")
    print("5. Подождите 1 час - не удалили ли пост")
    print("=" * 60)
    
    # Сохраняем результат
    with open('test_1_result.txt', 'w', encoding='utf-8') as f:
        f.write(f"Тест 1: {time.ctime()}\n")
        f.write(f"Message ID: {message.message_id}\n")
        f.write(f"Канал: {CHANNEL}\n")
        f.write(f"Статус: ОТПРАВЛЕНО\n")
        f.write(f"Ручной кросс-постинг: ТРЕБУЕТСЯ\n")
    
    print("\n💾 Результат сохранён в test_1_result.txt")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    
    with open('test_1_error.txt', 'w', encoding='utf-8') as f:
        f.write(f"Ошибка теста 1: {time.ctime()}\n")
        f.write(f"Ошибка: {str(e)}\n")