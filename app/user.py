from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from app.database.requests import set_user

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer(f'🤖 Добро пожаловать {message.from_user.first_name}, в $AI чат-бот!\n\nБот запоминает контекст при общении в чате и умеет работать с картинками.\n\nВнимание! Бот находится на стадии разработки. Если вы обнаружите ошибку, сообщите пожалуйста нам - @mrkorzun')