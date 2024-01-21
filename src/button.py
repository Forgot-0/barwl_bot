from aiogram import types

ids = ["Duels", "Hot-Zone", "Knockout", "Gem-Grab", "Duo-Showdown", "Heist", "Bounty", "Brawl-Ball", "Siege"]

name_ids = ["Дуэли", "Горячая Зона", "Нокаут", "Захват Кристаллов", "Парное Столкновение", "Ограбление", "Награда За Поимку", "Броулбол", 
"Осада"]

name_hero = ['Shelly', 'Nita', 'Colt', 'Bull', 'Jessie', 'Brock', 'Dynamike', 'Bo', 'Tick', '8-Bit', 'Emz', 'Stu', 'El-Primo', 'Barley', 
'Poco', 'Rosa', 'Rico', 'Darryl', 'Penny', 'Carl', 'Jacky', 'Piper', 'Pam', 'Frank', 'Bibi', 'Bea', 'Nani', 'Edgar', 'Griff', 'Grom', 
'Mortis', 'Tara', 'Gene', 'Max', 'Mr.P', 'Sprout', 'Byron', 'Squeak', 'Spike', 'Crow', 'Leon', 'Sandy', 'Amber', 'Meg', 'Gale', 'Surge', 
'Colette', 'Lou', 'Colonel-Ruffs', 'Belle', 'Buzz', 'Ash', 'Lola', 'Fang']

async def key_board():
	inline_kb = types.InlineKeyboardMarkup()
	for i in range(0, len(name_ids), 3):
		inline_btn = types.InlineKeyboardButton(name_ids[i], callback_data= ids[i])
		inline_btn1 = types.InlineKeyboardButton(name_ids[i+1], callback_data= ids[i+1])
		inline_btn2 = types.InlineKeyboardButton(name_ids[i+2], callback_data= ids[i+2])
		inline_kb.add(inline_btn, inline_btn1, inline_btn2)

	#inline_btn = types.InlineKeyboardButton("Одиночное Столкновение", callback_data= "Showdown")
	#inline_kb.add(inline_btn)
	return inline_kb

async def key_board1():
	inline_kb = types.InlineKeyboardMarkup()
	for i in range(0, len(name_ids), 3):
		inline_btn = types.InlineKeyboardButton(name_ids[i], callback_data= ids[i]+"1")
		inline_btn1 = types.InlineKeyboardButton(name_ids[i+1], callback_data= ids[i+1]+"1")
		inline_btn2 = types.InlineKeyboardButton(name_ids[i+2], callback_data= ids[i+2]+"1")
		inline_kb.add(inline_btn, inline_btn1, inline_btn2)
	inline_btn = types.InlineKeyboardButton("Одиночное Столкновение", callback_data= "Showdown1")
	inline_kb.add(inline_btn)

	return inline_kb

async def keyboard_name(spis):
	inline_kb = types.InlineKeyboardMarkup()
	for i in range(1):
		inline_btn = types.InlineKeyboardButton(spis[i], callback_data= spis[i])
		inline_btn1 = types.InlineKeyboardButton(spis[i+1], callback_data= spis[i+1])
		inline_btn2 = types.InlineKeyboardButton(spis[i+2], callback_data= spis[i+2])
		inline_kb.add(inline_btn, inline_btn1, inline_btn2)
	return inline_kb

async def name_hero(name, eng_name):
	inline_kb = types.InlineKeyboardMarkup()
	inline_btn = types.InlineKeyboardButton(name, callback_data = eng_name)
	inline_kb.add(inline_btn)
	return inline_kb