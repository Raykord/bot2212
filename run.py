import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command 
from aiogram.types import Message


bot = Bot(token="токен")
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello")

@dp.message(Command('help')) 
async def cmd_start(message: Message):
    await message.answer('''Commands: 
                         /start - старт 
                         /help - помощь''')
    
@dp.message(Command('анекдот'))
async def cmd_joke(message: Message):
    await message.answer('В дверь постучали 8 раз, осминог, подумал Штирлиц')   

@dp.message(F.text == 'привет')
async def hi_anwer(message: Message):
    await message.answer('Привет')

@dp.message(F.text.contains('Капибара'))
async def founded_kapibara(message: Message):
    await message.answer('Капиба́ра, или водосви́нка, — полуводное травоядное млекопитающее из подсемейства водосвинковых, один из двух ныне существующих видов рода водосвинки. Капибара — самый крупный среди современных грызунов.')

@dp.message(F.text)
async def echo(message: Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

