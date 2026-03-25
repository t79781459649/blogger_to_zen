#!/usr/bin/env python3
"""
ПЕРВЫЙ ТЕСТ - РАБОЧАЯ ВЕРСИЯ с python-telegram-bot
"""
import sys
import time
from telegram import Bot
from telegram.error import TelegramError

# === НАСТРОЙКИ ===
# ВАШ ТОКЕН от @BotFather
TOKEN = "8099475704:AAEtCKPDVy1ViVD20UzLc8AX01H2bjm8n-A"  # Вставьте сюда ваш токен
# ВАШ КАНАЛ (публичный: @имя или приватный: -1001234567890)
CHANNEL = "@anna_roses_crimea"  # Вставьте сюда ваш канал

def main():
    print("=" * 70)
    print("🌹 ПЕРВЫЙ ТЕСТОВЫЙ ЗАПУСК (python-telegram-bot)")
    print("=" * 70)
    
    if not TOKEN or TOKEN == "ВАШ_ТОКЕН_ЗДЕСЬ":
        print("❌ Токен не указан!")
        print("\nКак получить токен:")
        print("1. Откройте Telegram, найдите @BotFather")
        print("2. Отправьте: /newbot")
        print("3. Придумайте имя бота (например: RosesTestBot)")
        print("4. Скопируйте токен (выглядит как: 1234567890:ABCdef...)")
        print("\nВставьте токен в строку TOKEN = \"\" на 10-й строке этого файла")
        return
    
    if not CHANNEL:
        print("❌ Канал не указан!")
        print("\nУкажите ваш канал в строке CHANNEL = \"\"")
        print("Формат: @username для публичного или -100123... для приватного")
        return
    
    # 1. Создаём бота
    print("1. Создаём бота...")
    try:
        bot = Bot(token=TOKEN)
        
        # 2. Проверяем бота
        me = bot.get_me()
        print(f"   ✅ Бот подключен: @{me.username} (ID: {me.id})")
        
        # 3. Проверяем канал
        print(f"\n2. Проверяем доступ к каналу '{CHANNEL}'...")
        try:
            chat = bot.get_chat(chat_id=CHANNEL)
            print(f"   ✅ Канал найден: {chat.title}")
            
            # Проверяем права бота
            member = bot.get_chat_member(chat_id=CHANNEL, user_id=me.id)
            if member.status in ['administrator', 'creator']:
                print(f"   ✅ Бот является администратором канала")
            else:
                print(f"   ⚠️  Бот НЕ администратор! Добавьте бота в канал как администратора")
                print("   Права бота: " + member.status)
                
        except TelegramError as e:
            print(f"   ⚠️  Ошибка доступа к каналу: {e}")
            print(f"\nПроверьте:")
            print(f"1. Канал '{CHANNEL}' существует")
            print(f"2. Бот добавлен в канал")
            print(f"3. Для приватного канала: используйте ID (например -1001234567890)")
            print("\nПродолжаем тест...")
        
        # 4. Показываем тестовое сообщение
        print("\n3. Тестовое сообщение:")
        
        test_message = """[ТЕСТ_1] Проверка системы

Это тестовое сообщение для проверки работы бота.

После отправки:
1. Проверьте канал в Telegram
2. ВРУЧНУЮ сделайте кросс-постинг в Дзен (если нужно)
3. Ждите 24 часа

#тест #проверка #ботаник"""
        
        print("=" * 50)
        print(test_message)
        print("=" * 50)
        
        confirm = input("\nОтправить это сообщение? (да/нет): ").strip().lower()
        
        if confirm != 'да':
            print("❌ Отменено пользователем")
            return
        
        # 5. Отправляем сообщение
        print("\n🔄 Отправляю сообщение...")
        message = bot.send_message(
            chat_id=CHANNEL,
            text=test_message
        )
        
        print(f"✅ УСПЕХ!")
        print(f"📱 ID сообщения: {message.message_id}")
        print(f"📅 Дата сообщения: {message.date}")
        print(f"🕐 Время отправки: {time.ctime()}")
        
        # 6. Сохраняем результат
        result = f"""РЕЗУЛЬТАТ ПЕРВОГО ТЕСТА
==========================
Дата теста: {time.ctime()}
Бот: @{me.username} (ID: {me.id})
Канал: {CHANNEL}
Message ID: {message.message_id}
Дата сообщения: {message.date}
Статус: ОТПРАВЛЕНО

ЧТО ДЕЛАТЬ СЕЙЧАС:
1. 📱 Откройте Telegram
2. 🔍 Найдите канал: {CHANNEL}
3. ✅ Убедитесь, что сообщение появилось
4. 🔗 Если нужно - вручную сделайте кросс-постинг в Дзен
5. ⏳ Подождите 24 часа
6. 📝 Если всё ок - следующий тест

Следующий тест: фото + текст
==========================
"""
        
        with open('first_test_result.txt', 'w', encoding='utf-8') as f:
            f.write(result)
        
        print(f"\n💾 Результат сохранён в first_test_result.txt")
        
        print("\n" + "=" * 70)
        print("🎯 ВАШИ ДЕЙСТВИЯ СЕЙЧАС:")
        print(f"1. 📱 Откройте Telegram → канал '{CHANNEL}'")
        print("2. ✅ Убедитесь, что пост появился")
        print("3. 🔗 Нажмите 'Поделиться' → 'Дзен' (если нужно, ВРУЧНУЮ)")
        print("4. ⏳ Ждите 24 часа - не удалят ли")
        print("5. 📊 Завтра - тест с фото")
        print("=" * 70)
        
    except TelegramError as e:
        print(f"❌ Ошибка Telegram: {e}")
        
        with open('first_test_error.txt', 'w', encoding='utf-8') as f:
            f.write(f"Ошибка Telegram: {str(e)}\n")
            f.write(f"Время: {time.ctime()}\n")
            f.write(f"Токен: {TOKEN[:10]}...\n")
            f.write(f"Канал: {CHANNEL}\n")
            
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        
        with open('first_test_error.txt', 'w', encoding='utf-8') as f:
            f.write(f"Ошибка: {str(e)}\nВремя: {time.ctime()}")

if __name__ == "__main__":
    main()