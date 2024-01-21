from aiogram import Bot, Dispatcher, executor, types
from pars import *
from button import *

TOKEN = ""

bot = Bot(token= TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, """
    если играешь пати отправь команду - /team
    если играешь в соло отправь команду /solo
    """)#reply_markup = await key_board()

@dp.message_handler(commands=['team'])
async def start(message: types.Message):
	await bot.send_message(message.chat.id, "Выберите режим?", reply_markup = await key_board())

@dp.message_handler(commands=['solo'])
async def start(message: types.Message):
	await bot.send_message(message.chat.id, "Выберите режим?", reply_markup = await key_board1())


@dp.callback_query_handler()
async def process_callback_button1(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)

	if callback_query.data in ids:
		spis = map_bs(rejim(callback_query.data))
		photo = spis[0]
		name = spis[1]
		for i in range(5):
			gluing(photo[i]).save("out.jpg")
			await bot.send_photo(callback_query.message.chat.id, open("out.jpg", "rb"), reply_markup = await keyboard_name(name[i]))

	elif callback_query.data[-1] == "1":
		top = solo_game(rejim(callback_query.data[:-1]))
		for key in top.keys():
			eng_name = top[key][0].replace(".png", "").split("/")[-1]
			await bot.send_photo(callback_query.message.chat.id, top[key][0], reply_markup = await name_hero(top[key][-1], eng_name))

	elif callback_query.data in name_hero:
		pass


	else:
		pass

if __name__ == '__main__':
    executor.start_polling(dp)
