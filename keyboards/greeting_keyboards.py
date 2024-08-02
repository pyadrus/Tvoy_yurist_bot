from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def greeting_keyboards() -> InlineKeyboardMarkup:
    """Клавиатуры поста приветствия для всех пользователей"""
    keyboards_greeting = InlineKeyboardMarkup()
    question_1 = InlineKeyboardButton(text='Взыскание денег за некачественный ремонт', callback_data='question_1')
    keyboards_greeting.row(question_1)
    question_2 = InlineKeyboardButton(text='Взыскание денег за просрочку сдачи объекта', callback_data='question_2')
    keyboards_greeting.row(question_2)
    question_3 = InlineKeyboardButton(text='Избавление от кредитов и долгов', callback_data='question_3')
    keyboards_greeting.row(question_3)
    return keyboards_greeting


if __name__ == '__main__':
    greeting_keyboards()  # Клавиатура для пользователя
