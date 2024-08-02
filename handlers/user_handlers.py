import sqlite3
import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from system.dispatcher import dp, bot


class MakingAnOrder(StatesGroup):
    """Обработчик номера телефона и имени"""
    question_1_name = State()
    question_1_phone_number = State()
    question_2_name = State()
    question_2_phone_number = State()
    question_3_name = State()
    question_3_phone_number = State()


@dp.callback_query_handler(lambda c: c.data == 'question_1')
async def check_order_start_1(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Пожалуйста, введите ваше имя:")
    # Переходим в состояние ожидания ввода номера имени
    await MakingAnOrder.question_1_name.set()


@dp.message_handler(state=MakingAnOrder.question_1_name)
async def process_guest_number(message: types.Message, state: FSMContext):
    """Обработчик для ввода номера телефона"""
    await state.update_data(question_1_name=message.text)
    await bot.send_message(message.chat.id, "Введите номер телефона в формате +79999999999:")
    await MakingAnOrder.question_1_phone_number.set()


@dp.message_handler(state=MakingAnOrder.question_1_phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    """Обработчик для ввода номера телефона"""
    await state.update_data(question_1_phone_number=message.text)

    data = await state.get_data()
    guest_name = data.get('question_1_name')
    phone_number = data.get('question_1_phone_number')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message_text = (f"Спасибо, в ближайшее время мы свяжемся с Вами\n"
                    "\nДля возврата в начало нажмите /start")

    await bot.send_message(message.chat.id, message_text)

    admin_id = 6224881647

    message_text_admin = (f"<b>Данные:</b>\n"
                          f"Имя: {guest_name}\n"
                          f"Номер телефона: {phone_number}\n"
                          "Вопрос: Взыскание денег за некачественный ремонт\n")
    await bot.send_message(admin_id, message_text_admin, disable_web_page_preview=True)

    connection = sqlite3.connect('setting/orders.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_question (name, phone, question, timestamp)''')
    cursor.execute(
        "INSERT INTO user_question (name, phone, question, timestamp) VALUES (?, ?, ?, ?)",
        (guest_name, phone_number, "Взыскание денег за некачественный ремонт", str(current_time)))
    connection.commit()
    connection.close()

    await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'question_2')
async def check_order_start_2(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Пожалуйста, введите ваше имя:")
    # Переходим в состояние ожидания ввода номера заказа
    await MakingAnOrder.question_2_name.set()


@dp.message_handler(state=MakingAnOrder.question_2_name)
async def process_guest_number(message: types.Message, state: FSMContext):
    """Обработчик для ввода номера гостя"""
    await state.update_data(guest_name=message.text)
    await bot.send_message(message.chat.id, "Введите номер телефона в формате +79999999999:")

    await MakingAnOrder.question_2_phone_number.set()


@dp.message_handler(state=MakingAnOrder.question_2_phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    """Обработчик для ввода номера телефона"""
    await state.update_data(phone_number=message.text)

    data = await state.get_data()
    guest_name = data.get('guest_name')
    phone_number = data.get('phone_number')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message_text = (f"Спасибо, в ближайшее время мы свяжемся с Вами\n"
                    "\nДля возврата в начало нажмите /start")

    await bot.send_message(message.chat.id, message_text)

    admin_id = 6224881647

    message_text_admin = (f"<b>Данные:</b>\n"
                          f"Имя: {guest_name}\n"
                          f"Номер телефона: {phone_number}\n"
                          "Вопрос: Взыскание денег за просрочку сдачи объекта\n")
    await bot.send_message(admin_id, message_text_admin, disable_web_page_preview=True)

    connection = sqlite3.connect('setting/orders.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_question (name, phone, question, timestamp)''')
    cursor.execute(
        "INSERT INTO user_question (name, phone, question, timestamp) VALUES (?, ?, ?, ?)",
        (guest_name, phone_number, "Взыскание денег за просрочку сдачи объекта", str(current_time)))
    connection.commit()
    connection.close()

    await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'question_3')
async def check_order_start_3(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Пожалуйста, введите ваше имя:")
    await MakingAnOrder.question_3_name.set()


@dp.message_handler(state=MakingAnOrder.question_3_name)
async def process_guest_name(message: types.Message, state: FSMContext):
    """Обработчик для ввода имени гостя"""
    await state.update_data(guest_name=message.text)
    await bot.send_message(message.chat.id, "Введите номер телефона в формате +79999999999:")
    await MakingAnOrder.question_3_phone_number.set()


@dp.message_handler(state=MakingAnOrder.question_3_phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    """Обработчик для ввода номера телефона"""
    await state.update_data(phone_number=message.text)

    data = await state.get_data()
    guest_name = data.get('guest_name')
    phone_number = data.get('phone_number')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message_text = (f"Спасибо, в ближайшее время мы свяжемся с Вами\n"
                    "\nДля возврата в начало нажмите /start")

    await bot.send_message(message.chat.id, message_text)

    admin_id = 6224881647

    message_text_admin = (f"<b>Данные:</b>\n"
                          f"Имя: {guest_name}\n"
                          f"Номер телефона: {phone_number}\n"
                          "Вопрос: Избавление от кредитов и долгов\n")
    await bot.send_message(admin_id, message_text_admin, disable_web_page_preview=True)

    connection = sqlite3.connect('setting/orders.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_question (name, phone, question, timestamp)''')
    cursor.execute(
        "INSERT INTO user_question (name, phone, question, timestamp) VALUES (?, ?, ?, ?)",
        (guest_name, phone_number, "Избавление от кредитов и долгов", str(current_time)))
    connection.commit()
    connection.close()

    await state.finish()


def user_handler():
    """Регистрируем handlers для администратора"""
    dp.register_callback_query_handler(check_order_start_1)
    dp.register_callback_query_handler(check_order_start_2)
    dp.register_callback_query_handler(check_order_start_3)
