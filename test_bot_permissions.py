# test_bot_permissions.py
import telebot

TOKEN = "8099475704:AAEtCKPDVy1ViVD20UzLc8AX01H2bjm8n-A"
CHANNEL = "@anna_roses_crimea"

bot = telebot.TeleBot(TOKEN)

try:
    # Получаем информацию о боте
    me = bot.get_me()
    print(f"✅ Бот: @{me.username} (ID: {me.id})")
    
    # Пробуем получить информацию о канале
    try:
        chat = bot.get_chat(CHANNEL)
        print(f"✅ Канал найден: {chat.title}")
        
        # Проверяем права бота в канале
        member = bot.get_chat_member(CHANNEL, me.id)
        print(f"✅ Статус бота в канале: {member.status}")
        
        if member.status in ['administrator', 'creator']:
            print("✅ Бот является администратором канала!")
        else:
            print("❌ Бот НЕ администратор канала!")
            print("Добавьте бота в канал как администратора:")
            print("1. Откройте канал в Telegram")
            print("2. Настройки канала → Администраторы")
            print("3. Добавить администратора → выберите вашего бота")
            print("4. Дайте права: 'Отправлять сообщения'")
            
    except Exception as e:
        print(f"❌ Ошибка доступа к каналу: {e}")
        print(f"Проверьте что канал '{CHANNEL}' существует")
        print("И что бот добавлен в него")
        
except Exception as e:
    print(f"❌ Ошибка: {e}")
    print("Проверьте токен бота")