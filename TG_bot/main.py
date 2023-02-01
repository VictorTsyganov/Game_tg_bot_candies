from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import randint

bot = Bot('TOKEN')
disp = Dispatcher(bot)

async def on_start(_):
    print('Бот запущен.')

@disp.message_handler(commands=['help'])
async def mes_help(massage: types.Message):
    await massage.answer('Если хочешь играть, вводи команду /start_game')

@disp.message_handler(commands=['start_game'])
async def mes_start(massage: types.Message):
    await massage.answer('На столе лежит 128 конфет.'
    ' Играют два игрока делая ход друг после друга.'
    ' За один ход можно забрать не более чем 28 конфет.'
    ' Все конфеты оппонента достаются сделавшему последний ход.')
    await massage.answer('Делайте первый ход. (/take количество)')

value = 128

@disp.message_handler(commands=['take'])
async def take_from_value(massage: types.Message):
    global value
    count = int(massage.text.split()[1])
    if count in range(1, 29):
        value -= count
        if value > 28:
            await massage.answer(f'Количество конфет на столе после вашего хода: {value}')
        else:
            await massage.answer(f'Количество конфет на столе после вашего хода: {value}')
            await massage.answer('Победа бота!!!')
            value = 128
            
        bot_count = randint(1, 28)
        value -= bot_count
        if value > 28:
            await massage.answer(f'Бот взял {bot_count} конфет. Количество конфет на столе после хода бота: {value}')
        else:
            await massage.answer(f'Бот взял {bot_count} конфет. Количество конфет на столе после хода бота: {value}')
            await massage.answer('Вы победили!!!')
            value = 128
    else:
        await massage.answer('Количество конфет, которое можно брать, от 1 до 28. Повторите ход.')

executor.start_polling(disp, skip_updates=True, on_startup=on_start)
