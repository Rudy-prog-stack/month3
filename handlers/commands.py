from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from config import bot
from datetime import datetime
import random

jokes = ["Почему программист не любит природу? — Там слишком много багов.",
         "Что сказал ноль восьмёрке? — Классный ремень!",
         "Почему книга пошла к врачу? — У неё были проблемы с обложкой.",
         "Как называется грустный сыр? — Сыр-отик.",
         "Папа, а что такое ирония? — Спроси у мамы, она тебе объяснит. — Мам, что такое ирония? — Не мешай, я занята!",]

router_commands = Router()

@router_commands.message(Command('start'))
async def start_handler(message: Message):
    await message.answer('Привет мир!')

    await bot.send_message(chat_id=message.chat.id, 
                           text=f'Привет! {message.from_user.full_name} \nТвой телеграм ID > {message.from_user.id}')


@router_commands.message(F.text == 'привет')
async def hello_handler(message: Message):
    await message.answer('Салам')


@router_commands.message(Command('sticker'))
async def sticker_handler(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAM5auCySPyaBYsHzBJnxxDp79pfm1sAAqirAAKFa_lIF38CcJWB3Wg9BA')
    await message.answer_sticker(sticker='CAACAgIAAxkBAAM1auCx0ITQ88ljCxCaBsYQuKdB2vEAAuMAA1eEbA_LD3f9g8IMvD0E')



@router_commands.message(Command('mem'))
async def mem_handler(message: Message):
    photo = FSInputFile('media/image.png')
    await message.answer_photo(photo=photo)

@router_commands.message(Command('time'))
async def time_handler(message: Message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
    await message.answer(f"Сейчас: {current_time}")

@router_commands.message(Command('random'))
async def time_handler(message: Message):
    number = random.randint(1, 100)
    await message.answer(f"Твое число: {number}")

@router_commands.message(Command('joke'))
async def time_handler(message: Message):

    joke = random.choice(jokes)
    await message.answer(f"{joke}")

