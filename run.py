import asyncio
from random import randint
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command 
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from emoji import emojize
import keyboards as kb


class NeedWater(StatesGroup):
    liters = State()
    gaz = State()
    addres = State()


bot = Bot(token="")
dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(emojize("Hello"), reply_markup=kb.main)    

@dp.message(Command('help')) 
async def cmd_start(message: Message):
    await message.answer('''Commands: 
                         /start - старт 
                         /help - помощь''')
    
@dp.message(Command('анекдот'))
async def cmd_joke(message: Message):
    await message.answer('<b>В дверь постучали 8 раз, осминог, подумал Штирлиц</b>', parse_mode='HTML', reply_markup=kb.rick)   



@dp.message(F.text == 'привет')
async def hi_anwer(message: Message):
    await message.answer('Привет')

@dp.message(F.text.contains('Капибара'))
async def founded_kapibara(message: Message):
    await message.answer('<i><a href="https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BF%D0%B8%D0%B1%D0%B0%D1%80%D0%B0">Капиба́ра</a>, или <s>водосви́нка</s>, — <u>полуводное</u> травоядное млекопитающее из подсемейства водосвинковых, один из двух ныне существующих видов рода водосвинки. Капибара — самый крупный среди современных грызунов.</i>', parse_mode='HTML')


@dp.message(Command('roll'))
async def cmd_roll(message: Message):
    text = message.text
    try: #блок try ловит ошибки и если они есть, то выполняет код в блоке except
        number = text.split(' ') 
        if len(number) == 2: 
            result = randint(1, int(number[1]))
        else:
            result = randint(1, 100)
    except:
        result = randint(1, 100)
    await message.answer(f'Выпало: {result}')



@dp.message(Command('water'))
async def cmd_water(message: Message, state: FSMContext):
    await message.answer('Сколько литров воды?')
    await state.set_state(NeedWater.liters.state)



@dp.message(NeedWater.liters)
async def cmd_water_liters(message: Message, state: FSMContext):
    await state.update_data(liters=message.text)
    await message.answer('Нужен газ?', reply_markup=kb.gaz)
    await state.set_state(NeedWater.gaz.state)



@dp.message(NeedWater.gaz)
async def cmd_water_gaz(message: Message, state: FSMContext):
    if message.text.lower() == 'да':
        await state.update_data(gaz=True)
    else:
        await state.update_data(gaz=False)
    await message.answer('В каком городе?')
    await state.set_state(NeedWater.addres.state)



@dp.message(NeedWater.addres)
async def cmd_water_address(message: Message, state: FSMContext):
    await state.update_data(addres=message.text)
    data = await state.get_data()
    gaz = ''
    if data['gaz']:
        gaz = 'Нужен'
    else:
        gaz = 'Не нужен'
    await message.answer(f'Спасибо! Доставим вам воду по аддресу {data["addres"]}, {data["gaz"]} и {data["liters"]} литров')
    await state.clear()



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

