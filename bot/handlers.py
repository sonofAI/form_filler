from aiogram import Dispatcher, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from db import add_user

class FormState(StatesGroup):
    name = State()
    surname = State()
    email = State()
    phone = State()
    birth_date = State()

async def start_handler(message: Message, state: FSMContext):
    await message.answer("Введите имя:")
    await state.set_state(FormState.name)

async def name_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите фамилию:")
    await state.set_state(FormState.surname)

async def surname_handler(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await message.answer("Введите email:")
    await state.set_state(FormState.email)

async def email_handler(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите номер телефона:")
    await state.set_state(FormState.phone)

async def phone_handler(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Введите дату рождения (ДД.ММ.ГГГГ):")
    await state.set_state(FormState.birth_date)

async def birth_date_handler(message: Message, state: FSMContext):
    await state.update_data(birth_date=message.text)
    data = await state.get_data()
    add_user(data["name"], data["surname"], data["email"], data["phone"], data["birth_date"])
    await message.answer("Вы добавлены в очередь!")
    await state.clear()

def register_handlers(dp: Dispatcher):
    dp.message.register(start_handler, F.text == "/start")
    dp.message.register(name_handler, FormState.name)
    dp.message.register(surname_handler, FormState.surname)
    dp.message.register(email_handler, FormState.email)
    dp.message.register(phone_handler, FormState.phone)
    dp.message.register(birth_date_handler, FormState.birth_date)
