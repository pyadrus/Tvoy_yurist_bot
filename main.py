from aiogram import executor

from handlers.admin_handlers import admin_handler
from handlers.greeting_handlers import greeting_handler
from handlers.user_handlers import user_handler
from system.dispatcher import dp


def main():
    executor.start_polling(dp, skip_updates=True)
    greeting_handler()  # Начальное приветствие
    user_handler()  # Обработчик ввода имени и номера телефона
    admin_handler()


if __name__ == '__main__':
    try:
        main()  # Запуск бота
    except Exception as e:
        print(e)
