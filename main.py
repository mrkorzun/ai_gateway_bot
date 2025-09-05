import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.admin import admin
from app.user import user
from app.database.models import async_main

async def startup(dispatcher: Dispatcher):
    print('Bot starting up...')
    await async_main()
    
async def shuttdown(dispatcher: Dispatcher):
    print('Bot shutting down...')

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TG_TOKEN'))
    dp = Dispatcher()
    dp.startup.register(startup)
    dp.shutdown.register(shuttdown)
    dp.include_routers(admin, user)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped by user...')