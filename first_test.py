#!/usr/bin/env python3
"""
ПЕРВЫЙ ТЕСТ: проверка бота и канала
"""
# ВАЖНО: правильное имя пакета!
try:
    import telegram
    from telegram import Bot
    print("✅ Импорт через 'telegram' работает")
    USE_TELEGRAM = True
except ImportError:
    try:
        import telebot
        print("✅ Импорт через 'telebot' работает")
        USE_TELEGRAM = False
    except ImportError:
        print("❌ Ни один модуль не установлен!")
        exit(1)
import time

# === НАСТРОЙКИ ===
TOKEN = "8099475704:AAEtCKPDVy1ViVD20UzLc8AX01H2bjm8n-A"  # Например: 1234567890:ABCdefGHIjklMNO...
CHANNEL = "@anna_roses_crimea"     # Например: @roses_test_channel

def main():
    print("=" * 70)
    print("🌹 ПЕРВЫЙ ТЕСТОВЫЙ ЗАПУСК")
    print("=" * 70)
    
    # 1. Проверяем подключение
    print("1. Проверяем подключение к боту...")
    bot = telebot.TeleBot(TOKEN)
    
    try:
        me = bot.get_me()
        print(f"   ✅ Бот подключен: @{me.username}")
    except Exception as e:
        print(f"   ❌ Ошибка подключения: {e}")
        return
    
    # 2. Проверяем канал
    print("\n2. Проверяем доступ к каналу...")
    try:
        chat = bot.get_chat(CHANNEL)
        print(f"   ✅ Канал найден: {chat.title}")
    except Exception as e:
        print(f"   ❌ Ошибка доступа к каналу: {e}")
        print(f"   Убедитесь что канал '{CHANNEL}' существует")
        print(f"   И бот добавлен в него как администратор")
        return
    
    # 3. Отправляем тестовое сообщение
    print("\n3. Отправляем тестовое сообщение...")
    
    test_message = """[ТЕСТ_1] Проверка системы

Это тестовое сообщение для проверки работы бота.

После отправки:
1. Проверьте канал в Telegram
2. ВРУЧНУЮ сделайте кросс-постинг в Дзен
3. Ждите 24 часа

#тест #проверка #ботаник
"""
    
    print("=" * 50)
    print("Текст сообщения:")
    print("-" * 50)
    print(test_message)
    print("-" * 50)
    
    confirm = input("\nОтправить это сообщение? (да/нет): ").strip().lower()
    
    if confirm != 'да':
        print("❌ Отменено пользователем")
        return
    
    try:
        print("\n🔄 Отправляю сообщение...")
        message = bot.send_message(CHANNEL, test_message)
        
        print(f"✅ УСПЕХ!")
        print(f"📱 ID сообщения: {message.message_id}")
        print(f"🕐 Время: {time.ctime()}")
        
        # Сохраняем результат
        result = f"""РЕЗУЛЬТАТ ПЕРВОГО ТЕСТА
==========================
Дата: {time.ctime()}
Бот: @{me.username}
Канал: {CHANNEL}
Message ID: {message.message_id}
Статус: ОТПРАВЛЕНО

ЧТО ДЕЛАТЬ:
1. Откройте Telegram → ваш канал
2. Убедитесь что сообщение есть
3. Нажмите "Поделиться" → "Дзен"
4. Проверьте что пост появился в Дзен
5. Ждите 24 часа

Следующий тест через 24 часа.
"""
        
        with open('first_test_result.txt', 'w', encoding='utf-8') as f:
            f.write(result)
        
        print(f"\n💾 Результат сохранён в first_test_result.txt")
        
        print("\n" + "=" * 70)
        print("🎯 ВАШИ ДЕЙСТВИЯ СЕЙЧАС:")
        print("1. 📱 Откройте Telegram")
        print("2. 🔍 Найдите свой канал")
        print("3. ✅ Убедитесь, что пост появился")
        print("4. 🔗 Нажмите 'Поделиться' → 'Дзен' (ВРУЧНУЮ)")
        print("5. ⏳ Ждите 24 часа - не удалят ли")
        print("=" * 70)
        
    except Exception as e:
        print(f"❌ Ошибка отправки: {e}")
        
        with open('first_test_error.txt', 'w', encoding='utf-8') as f:
            f.write(f"Ошибка: {str(e)}\nВремя: {time.ctime()}")

if __name__ == "__main__":
    main()