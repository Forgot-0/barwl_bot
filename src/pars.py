import requests
from difflib import SequenceMatcher
from bs4 import BeautifulSoup
from PIL import Image

headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
	}

def gluing(spis):
	img = Image.new('RGB', (180*len(spis), 175))
	for i in range(len(spis)):
		img1 = Image.open(requests.get(spis[i], stream=True).raw)
		img.paste(img1, (180*i,0))

	return img

def rejim(idishnik):

	url = f"https://brawlify.com/ru/maps/"

	r = requests.get(url=url, headers=headers)
	soup = BeautifulSoup(r.text, "lxml")

	if idishnik == "Showdown":
		i = 2
	else:
		i = 0

	return soup.find("div", id = idishnik).find("div", class_ = f"map-def col-6 col-md-4 col-lg-3 map-block mb-{i}").find("a", class_= "link")["href"]

def map_bs(link):

	url = f"https://brawlify.com/{link}"

	r = requests.get(url=url, headers=headers)
	soup = BeautifulSoup(r.text, "lxml")

	content = soup.find("div", id = "teams").find_all("img")

	img = []
	name = []
	for i in range(0, len(content)-3, 3):
		img.append([content[i]["src"], content[i+1]["src"], content[i+2]["src"]])
		name.append([content[i]["alt"], content[i+1]["alt"], content[i+2]["alt"]])

	return img, name

def solo_game(link):
	url = f"https://brawlify.com{link}"#f"https://brawlify.com/{link}"
	print(url)
	#https://brawlify.com/ru/gamemodes/detail/Hot-Zone
	r = requests.get(url=url, headers=headers)
	soup = BeautifulSoup(r.text, "lxml")

	content = soup.find("tbody", class_ = "text-hp")

	main_content = content.find_all("tr")

	top_10 = {
	"1": [],
	"2": [],
	"3": [],
	"4": [],
	"5": [],
	"6": [],
	"7": [],
	"8": [],
	"9": [],
	"10": [],
	}

	for i in range(len(main_content)):
		n = main_content[i].find_all("td")[1]["class"][-1][-2:].replace("k", "")
		if n in top_10:
			top_10[n].append(main_content[i].img["src"])
			top_10[n].append(main_content[i].img["alt"])

	return top_10

def info_about_hero(name_hero):
	url = f"https://brawlify.com/ru/brawlers/detail/{name_hero}"

	r = requests.get(url=url, headers=headers)
	soup = BeautifulSoup(r.text, "lxml")

	
	return soup.find_all("table")


if __name__ == '__main__':
	print(info_about_hero("Barley"))