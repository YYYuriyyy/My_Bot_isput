import json

import telebot
from telebot import types

bot = telebot.TeleBot("6547985068:AAEjq1VX5mdF7sonGqeZYBcmZzV9sCpOrIo", parse_mode="html")
print("start")

counter = {
    "next_back": 0
}

texts = {
    "bot_info": "інфо про бота",
    "user_info": "інфо про користувача",
    "marshrut_1": """Цікаві та пізнавальні маршрути ТрускавцяМісто цілющих джерел, старовинної архітектури та легенд. 
    Дозвольте собі відпочити у Трускавці. Курортний сезон у Трускавці триває впродовж цілого року. 
    Незалежно від пори року чи погодних умов місто має чим зацікавити відпочивальників. 
    Саме тому у Трускавець з’їжджаються туристи як з України, так і з усього світу. 
    Тут Ви не лише проведете хорошу відпустку, а й зможете зміцнити своє здоров’я.""",

    "marshrut_2": ' "Музей історії Трускавця" ',

    "marshrut_3": ' "Екскурсія в Урич та Східницю" ',

    "marshrut_4": ' "Скелі Довбуша" ',

    "marshrut_5": ' "Львів оглядовий" '
}


def main_reply_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton("🙈Inline Menu"), types.KeyboardButton("Next"))
    markup.row(types.KeyboardButton("📍Ask me?"))
    markup.row(types.KeyboardButton("Info"))

    return markup


def info_reply_menu():
    info_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info_markup.row(types.KeyboardButton("Info bot"), types.KeyboardButton("Info user"))
    info_markup.row(types.KeyboardButton("Back"))

    return info_markup


def sub_reply_menu():
    sub_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sub_markup.row(types.KeyboardButton("Трускавець"))
    sub_markup.row(types.KeyboardButton("Back"))

    return sub_markup


def marshrut_reply_menu():
    sub_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sub_markup.row(types.KeyboardButton("(Оглядовий Трускавець) Маршрут №1"),
                   types.KeyboardButton("(Музеї історії) Маршрут №2"),
                   types.KeyboardButton("Екскурсійні тури з Трускавця"))
    sub_markup.row(types.KeyboardButton("Back"))

    return sub_markup

def menu():
    sub_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sub_markup.row(types.KeyboardButton("Урич та Східниця"),
                   types.KeyboardButton("Скелі Довбуша"),
                   types.KeyboardButton("Львів оглядовий"))
    sub_markup.row(types.KeyboardButton("Back"))

    return sub_markup


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт, як справи ?", reply_markup=main_reply_menu())


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    cid = message.chat.id
    if message.text == "📍Ask me?":
        mess = bot.send_message(cid, "Input your name: ")
        bot.register_next_step_handler(mess)
    elif message.text == "🙈Inline Menu":
        bot.send_message(cid, "🙈", reply_markup=i_test_menu())
    elif message.text == "Info":
        bot.send_message(cid, "🙈", reply_markup=info_reply_menu())
        counter["next_back"] += 1
    elif message.text == "Трускавець":
        bot.send_message(cid, "Виберіть маршрут", reply_markup=marshrut_reply_menu())
        counter["next_back"] += 1
    elif message.text == "Екскурсійні тури з Трускавця":
        bot.send_message(cid, "Виберіть маршрут", reply_markup=menu())
        counter["next_back"] += 1

    # - переміщення по боту

    elif message.text == "Next" and counter["next_back"] == 0:
        bot.send_message(cid, "🙈", reply_markup=sub_reply_menu())
        counter["next_back"] += 1
    elif message.text == "Back" and counter["next_back"] == 1:
        bot.send_message(cid, "🙈", reply_markup=main_reply_menu())
        counter["next_back"] -= 1
    elif message.text == "Back" and counter["next_back"] == 2:
        bot.send_message(cid, "🙈", reply_markup=sub_reply_menu())
        counter["next_back"] -= 1
    elif message.text == "Back" and counter["next_back"] == 3:
        bot.send_message(cid, "🙈", reply_markup=sub_reply_menu())
        counter["next_back"] -= 2
    elif message.text == "Back" and counter["next_back"] == 4:
        bot.send_message(cid, "🙈", reply_markup=sub_reply_menu())
        counter["next_back"] -= 2


    # - інфо

    elif message.text == "Info bot" and counter["next_back"] == 1:
        bot.send_message(cid, texts["bot_info"], reply_markup=info_reply_menu())
    elif message.text == "Info user" and counter["next_back"] == 1:
        bot.send_message(cid, texts["user_info"], reply_markup=info_reply_menu())
    elif message.text == "Info user" and counter["next_back"] == 1:
        bot.send_message(cid, texts["user_info"], reply_markup=info_reply_menu())
    elif message.text == "Info user" and counter["next_back"] == 1:
        bot.send_message(cid, texts["user_info"], reply_markup=info_reply_menu())
    elif message.text == "Info user" and counter["next_back"] == 1:
        bot.send_message(cid, texts["user_info"], reply_markup=info_reply_menu())


    # - Машрути

    elif message.text == "(Оглядовий Трускавець) Маршрут №1":
        bot.send_message(cid, texts["marshrut_1"], reply_markup=marshrut_reply_menu())
        photo = open('imgs/gallery_big_103408.jpg', 'rb')
        bot.send_photo(cid, photo, reply_markup=marshrut_reply_menu())
        photo = open('imgs/ww.jpg', 'rb')
        bot.send_photo(cid, photo, reply_markup=marshrut_reply_menu())
        photo = open('imgs/im-park_adamivka2.jpg', 'rb')
        bot.send_photo(cid, photo, reply_markup=marshrut_reply_menu())
        photo = open('imgs/606_173768_view (1).jpg', 'rb')
        bot.send_photo(cid, photo, reply_markup=marshrut_reply_menu())

    elif message.text == "(Музеї історії) Маршрут №2":
        bot.send_message(cid, texts["marshrut_2"], reply_markup=marshrut_reply_menu())
        photo_one = open('imgs/606_173768_view (1).jpg', 'rb')
        photo_two = open('imgs/606_173761_view.jpg', 'rb')
        photo_three = open('imgs/2019-01-10.jpg', 'rb')
        photo_four = open('imgs/2021-08-10.jpg', 'rb')
        photos = [types.InputMediaPhoto(photo_one), types.InputMediaPhoto(photo_two),
                  types.InputMediaPhoto(photo_three), types.InputMediaPhoto(photo_four, caption="""Музей історії Трускавця
    Через експозицію музею відвідувачі дізнаються про Середньовічний Трускавець княжих часів та польських королів;
    шляхетний Трускавець часів Австро-Угорщини та Польської держави, 
    коли був заснований та зміцнював свої позиції курорт в Європі; 
    місто-курорт Трускавець радянської доби та незалежної України, славний своїми цілющими мінеральними водами, 
    які підтримують його заслужену славу вже майже 200 років.Окрім експозиційних кімнат в музеї є дві виставкові зали, 
    в яких організовуються різноманітні виставки мистецького та краєзнавчого спрямування, 
    а також великий лекційний зал, де проводяться культурно-просвітницькі заходи.""")]

        bot.send_media_group(cid, photos)

    elif message.text == "Урич та Східниця":
        bot.send_message(cid, texts["marshrut_3"], reply_markup=menu())
        photo_one = open('imgs/QWW.jpg', 'rb')
        photo_two = open('imgs/2017.04.184479.jpg', 'rb')
        photo_three = open('imgs/QWWW.jpg', 'rb')
        photos = [types.InputMediaPhoto(photo_one),types.InputMediaPhoto(photo_two),
                  types.InputMediaPhoto(photo_three, caption="""
    Одна з коротких, але цікавих екскурсій в ближні Карпати зі знайомством і дегустацією мінеральних вод курорту Східниця, 
    національним парком «Сколівські Бескиди» і залишками фортеці «Тустань» (12 століття). Прогулянка по скельному масиву, 
    колишній язичницький жертовник, прекрасні панорами Карпат і джерело святої води. Вільний час. 
    За бажанням бойківська кухня.""")]

        bot.send_media_group(cid, photos)

    elif message.text == "Скелі Довбуша":
        bot.send_message(cid, texts["marshrut_4"], reply_markup=menu())
        photo_one = open('imgs/фф.webp', 'rb')
        photo_two = open('imgs/unnamed.jpg', 'rb')
        photo_three = open('imgs/EEE.jpg', 'rb')
        photo_four = open('imgs/Dovbysh_4.jpg', 'rb')
        photos = [types.InputMediaPhoto(photo_one), types.InputMediaPhoto(photo_two),
                  types.InputMediaPhoto(photo_three), types.InputMediaPhoto(photo_four, caption="""Одна з самих цікавих екскурсій в Карпати Івано-Франківської області.
                   У програмі екскурсії: знайомство з містом Стрий та курортом Моршин, каскадними водоспадами на річці Суккіль, 
                   «Кам’яним дивом Карпат» – скелями Довбуша в урочищі Соколине. Пішохідна екскурсія тривалістю 1,5 години, 
                   відвідування печер Довбуша, різноманітність скель з назвами і легендами. Неповторна панорама Карпат. 
                   Бойківська-гуцульська кухня гуцульських колиб.""")]

        bot.send_media_group(cid, photos)

    elif message.text == "Львів оглядовий":
        bot.send_message(cid, texts["marshrut_5"], reply_markup=menu())
        photo_one = open('imgs/Lviv_1.jpg', 'rb')
        photo_two = open('imgs/Lviv_2.jpg', 'rb')
        photo_three = open('imgs/Lviv_3.jpg', 'rb')
        photos = [types.InputMediaPhoto(photo_one), types.InputMediaPhoto(photo_two),
                  types.InputMediaPhoto(photo_three, caption="""Львів – одне з найстаріших міст Західної України, 
                  на території якого збереглося близько третини пам’ятників архітектури України. 37 музеїв, 6 театрів, 
                  старовинні вузькі вулички, музеї-кафетерії. Щорічно Львів відвідують десятки тисяч туристів зі всього світу. 
                  Львів – це дійсно музей під відкритим небом""")]

        bot.send_media_group(cid, photos)


bot.infinity_polling()
