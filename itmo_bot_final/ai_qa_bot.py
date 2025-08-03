# TG BOT
import telebot
from rag_pipeline import answer_question

TELEGRAM_TOKEN = '***'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Welcome Message
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я помогу тебе разобраться в программах магистратуры "Искусственный интеллект" и "Управление ИИ-продуктами". '
                          'Задавай мне любые вопросы по данным программам, или расскажи о себе, а я порекоммендую тебе подходящую программу!')


# Response to Query
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text.strip()

    try:
        response = answer_question(user_input)
        bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, f"Ошибка при обработке запроса: {e}")


if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
