import os
import time
import secrets
import requests
import telebot
import py_compile
import random
import json
import base64
import marshal
import zlib
from telebot import *
from telebot import util
from telebot import types
import user_agent
tokin = "5190512155:AAFB1_YRSPb3Hxi17F6ntkKMBMMzwYg2DOY" 

def check_user(user_id):
    global tokin
    request = requests.get(f"https://api.telegram.org/bot{tokin}/getChatMember?chat_id=@TezkorXabarlar_Olami&user_id={user_id}").text
    if '"status":"left"' in request or '"Bad Request: USER_ID_INVALID"' in request or '"status":"kicked"' in request or 'user not found' in request:
        return False
    else:
        return True



bot = telebot.TeleBot(tokin)
@bot.message_handler(commands=['start'])
def welcome(message):
    channel = types.InlineKeyboardButton(text=" Kanalimiz Developer ", url=f"https://t.me/TezkorXabarlar_Olami")
    if check_user(message.from_user.id):
        start = types.InlineKeyboardButton(text="Gif yasash ", callback_data="Start")
        programmer = types.InlineKeyboardButton(text=" 👨🏻‍💻 Developer ", url=f"https://t.me/py_run")
        Keyboards = types.InlineKeyboardMarkup()
        Keyboards.row_width = 2
        Keyboards.add(start, programmer, channel)
        bot.send_message(message.chat.id, text=f"Assalomu alaykum {message.from_user.first_name} Sizni korganimizdan hursandmiz O'zingizga kerakli bo'limni tanlang", reply_to_message_id=(message.message_id), reply_markup=Keyboards)
    else:
        Keyboard = types.InlineKeyboardMarkup()
        Keyboard.row_width = 1
        Keyboard.add(channel)
        
        bot.reply_to(message, text=f"💖| Assalomu Alaykum {message.from_user.first_name} \n🔰| Hush kelibsiz botimizdan foydalanish uchun kanalimizga A'zo bolib qayta /start bosing", reply_markup=Keyboard)
        
def start(message):
    channel = types.InlineKeyboardButton(text="Kanalimiz ", url=f"https://t.me/off_python")
    programmer = types.InlineKeyboardButton(text=" 👨🏻‍💻 admin ", url=f"https://t.me/py_run")
    Key = types.InlineKeyboardMarkup()
    Key.row_width = 2
    Key.add(channel, programmer)
    bot.edit_message_text(text=f"""💖| Assalom {message.from_user.first_name} O'zingizga kerakli bo'limni tanlang
◆━━━━━◆ ✲ ◆━━━━━◆
 1 )Gif yasash >>> /gif
 2 ) info Name >>> /info
 
◆━━━━━◆ ✲ ◆━━━━━◆""", chat_id=int(message.chat.id), message_id=message.message_id, reply_markup=Key)




@bot.message_handler(commands=['info'])
def info_get(message):
    channel = types.InlineKeyboardButton(text=" Kanalimiz ", url=f"https://t.me/off_python")
    programmer = types.InlineKeyboardButton(text=" 👨🏻‍💻 Admin ", url=f"https://t.me/py_run")
    Inline = types.InlineKeyboardMarkup()
    Inline.row_width = 2
    Inline.add(channel, programmer)
    bot.send_photo(message.chat.id,f"https://t.me/{message.from_user.username}",f"""
◆━━━━━◆ ✲ ◆━━━━━◆
✲ ID : `{message.from_user.id}`
◆━━━━━◆ ✲ ◆━━━━━◆
✲ Name : `{message.chat.first_name}`
◆━━━━━◆ ✲ ◆━━━━━◆
✲ user : `@{message.from_user.username}`
◆━━━━━◆ ✲ ◆━━━━━◆""", parse_mode="markdown", reply_markup=Inline)

@bot.message_handler(commands=['gif'])
def info_get(message):
    channel = types.InlineKeyboardButton(text=" Developer ", url=f"https://t.me/py_run")
    programmer = types.InlineKeyboardButton(text=" 👨🏻‍💻 Developer ", url=f"https://t.me/Off_python")
    Inline = types.InlineKeyboardMarkup()
    Inline.row_width = 2
    Inline.add(channel, programmer)
    bot.send_photo(message.chat.id,f"https://t.me/{message.from_user.username}",f"""{message.from_user.first_name} O'z ismingizga Gif yasash uchun ismingizni menga yuboring""", parse_mode="markdown", reply_markup=Inline)




@bot.message_handler(func=lambda m:True)
def mgit(message):
    text = message.text
    url = 'https://cooltext.com/PostChange'
    headers = {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
               'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://cooltext.com',
               'referer': 'https://cooltext.com/Logo-Design-Animated-Glow', 'sec-fetch-dest': 'empty',
               'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'sec-gpc': '1',
               'user-agent': user_agent.generate_user_agent(), 'x-requested-with': 'XMLHttpRequest'}
    data = {
        'LogoID': '26',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo1 = (r.json()['renderLocation'])
    data = {
        'LogoID': '4',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo2 = (r.json()['renderLocation'])
    data = {
        'LogoID': '819721038',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo3 = (r.json()['renderLocation'])
    data = {
        'LogoID': '1169711118',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo4 = (r.json()['renderLocation'])
    data = {
        'LogoID': '819515844',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo5 = (r.json()['renderLocation'])
    data = {
        'LogoID': '790967832',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo6 = (r.json()['renderLocation'])
    bot.send_video(message.chat.id,logo1)
    bot.send_video(message.chat.id,logo2)
    bot.send_video(message.chat.id,logo3)
    bot.send_video(message.chat.id,logo4)
    bot.send_video(message.chat.id,logo5)
    bot.send_video(message.chat.id,logo6)
    bot.send_message(message.chat.id,f"Done!")
    pass


@bot.callback_query_handler(func=lambda call: True)
def callbacks_data(call):
    if call.data == "Start":
        start(call.message)
    if call.data == "gif":
        sal(call.message)

while True:
    try:
        print("Done")
        bot.polling(True)
        break
    except Exception as ex:
        print(f"Error polling : {ex}")
        telebot.logger.error(ex)
        continue
