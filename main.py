import telebot
from telebot import types
from getdata import token
import webbrowser
import telebot
import settings
from IOData import save_users_to_json, add_user_to_json
import datetime


bot = telebot.TeleBot(token)
admin_id = 653372350
zakaz_id = 655465
game_static = {}
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Автосервис🔧")
    btn2 = types.KeyboardButton("Запчасти ⚙️")
    btn3 = types.KeyboardButton(f"Кузовной \n Ремонт\n 🚗")
    btn4 = types.KeyboardButton("Акции\n 💥")
    btn5 = types.KeyboardButton("Перейти на сайт\n 🌐")
    btn6 = types.KeyboardButton("Контакты\n☎️")
    markup.row(btn1, btn2,btn3)
    
    markup.row(btn4,btn5,btn6)
    # file = open('./TAHO.jpg','rb')
    # bot.send_photo(message.chat.id,reply_markup=markup)
    bot.send_message(message.chat.id, f'Добрый день, {message.from_user.first_name}', reply_markup=markup)
    bot.register_next_step_handler(message, menu_button)

def menu_button(message):
        message.text == "Автосервис🔧"
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Замена масла")
        btn2 = types.KeyboardButton("Диагностика")
        btn3 = types.KeyboardButton("Техобслуживание")
        btn4 = types.KeyboardButton("Подвеска")
        btn5 = types.KeyboardButton("Двигатель")
        btn6 = types.KeyboardButton("Тормозная система")
        btn7 = types.KeyboardButton("Трасмиссия")
        btn8 = types.KeyboardButton("Электрооборудование")
        btn9 = types.KeyboardButton("Кондиционер")
        btn10 = types.KeyboardButton("Рулевое управление")
        btn11 = types.KeyboardButton("Выхлопная система")
        btn12 = types.KeyboardButton("Допоборудование")
        markup.row(btn1, btn2,btn3)
        markup.row(btn4,btn5,btn6)
        markup.row(btn7,btn8, btn9)
        markup.row(btn10,btn11, btn12)
        bot.send_message(message.chat.id,f'Выберите услугу',reply_markup=markup)
        bot.register_next_step_handler(message, autoservis_button)
            

"""elif message.text == "Запчасти ⚙️":
        bot.send_message(message.chat.id, 'Скоро с вами свяжется наш менеджер')
    elif message.text == "Перейти на сайт\n 🌐":
        webbrowser.open('https://vostok-auto.ru/')
    elif message.text == "Контакты☎️":
        bot.send_message(message.chat.id, 'Скоро с вами свяжется наш менеджер')
    
        bot.register_next_step_handler(message, autoservis_button)"""

def autoservis_button(message):
    if message.text == "Замена масла":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("В Двигателе")
        btn2 = types.KeyboardButton("В АКПП")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,f'Выберите услугу',reply_markup=markup)
        bot.register_next_step_handler(message,Oil_In_Engine)
        

def Oil_In_Engine(message):
    if message.text == "В Двигателе":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Записаться на услугу")
        usluga = 'changing engine oil'
        markup.add(btn1)
        bot.send_message(message.chat.id,'<b>Замена масла в двигателе</b> <em>500 ₽</em>\n\n<b>Замена масла в двигателе</b><em> 750 ₽</em>\n<em>если клиент предоставит своё масло</em>', parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message,save_number1,usluga)

def save_number1(message,usluga):
    
    bot.send_message(message.chat.id,'Для оформления заказа и передачи его менеджеру просим '
                                                        'ввести ваш контактный номер (с помощью клавиатуры).')
    bot.register_next_step_handler(message,save_number,usluga)

    
def save_number(message,usluga):
        number = message.text
        
        if len(str(number)) >= 10 and ('+' in (str(number)) or '7' in (str(number)) or '8' in (str(number))): # проверка Номера на правильность Написания
            zayavka_done(bot=bot, message=message, number=number,usluga=usluga)
        else:
            bot.send_message(message.chat.id, 'указан некорректный номер.')
            kb4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            but1 = types.KeyboardButton(text='Вернуться в начало')
            kb4.add(but1)
            mes_num = bot.edit_message_reply_markup(message.chat.id, 'Для оформления заказа и передачи его менеджеру просим '
                                                        'ввести ваш контактный номер (с помощью клавиатуры).',
                                    reply_markup=kb4)
            bot.register_next_step_handler(mes_num, save_number1(message,usluga))

def zayavka_done(bot, message, number,usluga):
    try:
        bot.send_message(message.chat.id,
                         f'Вашему заказу присвоен номер {zakaz_id}. Заказ отправлен менеджеру.\n'
                         f'Дождитесь обратного звонка в ближайшее время, для уточнения деталей заказа.')
        
        bot.send_message(admin_id, f'🚨!!!ВНИМАНИЕ!!!🚨\n'                                    # Отправка заявки Админу
                                   f'Поступила ЗАЯВКА от:\n'
                                   f'id чата: {message.chat.id}\n'
                                   f'Имя: {message.chat.first_name}\n'
                                   f'Фамилия: {message.chat.last_name}\n'
                                   f'№ телефона: {number}\n'
                                   f'Ссылка: {usluga}\n')
        bot.send_message(admin_id, 'Заявка внесена в базу ✅\n'
                                   'смотреть базу: https://docs.google.com/spreadsheets/d/'
                                   '14P5j3t4Z9kmy4o87WEbLqeTwsKi7YZAx7RiQPlY2c1w/edit?usp=sharing')
        
        save_users_to_json( {'user_ID': message.chat.id, 'telephone': number,
                            'Firstname': message.chat.first_name, 'usluga' : usluga,
                            'time' : datetime.datetime.today().strftime("%d-%b-%Y (%H:%M)")}, 'zayavka.json')
        print(number)
    except Exception:
        bot.send_message(message.chat.id, 'Ошибка подключения. Повторите запрос через 1 минуту.')
        

# Дальше Шляпа

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти на сайт", url = 'https://vostok-auto.ru/')
    btn2 = types.InlineKeyboardButton("удалить фото", callback_data='delete')
    btn3 = types.InlineKeyboardButton("изменить текст", callback_data='edit')
    markup.row(btn1)
    markup.row(btn2,btn3)

    bot.reply_to(message, 'Какое красивое фото!',reply_markup = markup)

@bot.message_handler(commands=['start', 'main' , 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'ПРИВЕТ, {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>help</b> <em>information</em>', parse_mode='html')

@bot.callback_query_handler(func=lambda callback: True)
def collback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot. edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
       bot.send_message(message.chat.id, f'ПРИВЕТ, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, f'не верный формат')
        bot.register_next_step_handler(message, summa)
        return # что бы следующий код не выполнялся

bot.polling(none_stop=True)