from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Addlesson(StatesGroup):
    name = State()
    age = State()
    phone = State()

router_add_lesson = Router()


@router_add_lesson.message(Command('add_lesson'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('Введите свое имя:')
    await state.set_state(Addlesson.name)


@router_add_lesson.message(Addlesson.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите свой возраст:')
    await state.set_state(Addlesson.age)


@router_add_lesson.message(Addlesson.age)
async def add_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой телефон:')
    await state.set_state(Addlesson.phone)


@router_add_lesson.message(Addlesson.phone)
async def add_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    
    data = await state.get_data()

    await message.answer(f"Пользователь:{data['name']}\n Возраст:{data['age']} \n Телефон:{data['phone']}")

    await state.clear()
