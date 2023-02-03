from create import disp
from aiogram import types
from random import randint
from keyboards import kb_main_menu
from datetime import datetime

value = 128

@disp.message_handler(commands=['start'])
async def mes_help(message: types.Message):
    await message.answer('Рад Вас приветствовать!', reply_markup=kb_main_menu)
    user = []
    now = datetime.now()
    time_format = "%Y-%m-%d %H:%M:%S"
    user.append(f'{now:{time_format}}')
    user.append(message.from_user.username)
    user.append(message.from_user.full_name)
    user.append(message.from_user.id)
    user = list(map(str, user))
    with open('info.txt', 'a', encoding='UTF-8') as data:
        data.write(':'.join(user) + '\n')

@disp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Если хочешь играть, вводи команду /start_game')

@disp.message_handler(commands=['loc'])
async def mes_help(message: types.Message):
    await message.answer(message)

@disp.message_handler(content_types='location')
async def mes_help(message: types.Message):
    user = []
    now = datetime.now()
    time_format = "%Y-%m-%d %H:%M:%S"
    user.append(f'{now:{time_format}}')
    user.append(message.from_user.username)
    user.append(message.from_user.full_name)
    user.append(message.from_user.id)
    user.append(message.location)
    user = list(map(str, user))
    with open('info.txt', 'a', encoding='UTF-8') as data:
        data.write(':'.join(user) + '\n')

@disp.message_handler(commands=['start_game'])
async def mes_start(message: types.Message):
    global value
    await message.answer(f'На столе лежит {value} конфет.'
    ' Играют два игрока делая ход друг после друга.'
    ' За один ход можно забрать не более чем 28 конфет.'
    ' Все конфеты оппонента достаются сделавшему последний ход.')
    await message.answer('Делайте первый ход.')
    
@disp.message_handler()
async def take_from_value(message: types.Message):
    global value
    if message.text.isdigit():
        count = int(message.text)
        if count in range(1, 29):
            value -= count
            if value > 28:
                await message.answer(f'Количество конфет на столе после вашего хода: {value}')
            else:
                await message.answer(f'Количество конфет на столе после вашего хода: {value}')
                await message.answer('Победа бота!!!')
                value = 128

            if value != 128:    
                if value % 29 == 0:
                    bot_count = randint(1, 29)
                else:
                    bot_count = value - (value // 29) * 29
                # bot_count = randint(1, 28)
                value -= bot_count
                if value > 28:
                    await message.answer(f'Бот взял {bot_count} конфет. Количество конфет на столе после хода бота: {value}')
                else:
                    await message.answer(f'Бот взял {bot_count} конфет. Количество конфет на столе после хода бота: {value}')
                    await message.answer('Вы победили!!!')
                    value = 128
                
        else:
            await message.answer('Количество конфет, которое можно брать, от 1 до 28. Повторите ход.')