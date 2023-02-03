from handlers import disp
from aiogram.utils import executor


async def on_start(_):
    print('Бот запущен.')

executor.start_polling(disp, skip_updates=True, on_startup=on_start)
