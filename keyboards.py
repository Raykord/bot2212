from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='Выберите что-нибудь', one_time_keyboard=True, keyboard=[
    [KeyboardButton(text='Капибара'), KeyboardButton(text='1')],
    [KeyboardButton(text='анекдот')],
    [KeyboardButton(text='анекдот'), KeyboardButton(text='2'), KeyboardButton(text='3')]
])

gaz = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='Газ надо?', one_time_keyboard=True, keyboard=[
    [KeyboardButton(text='Да'), KeyboardButton(text='Нет')]
])


rick = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Нажми', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')]
    ])