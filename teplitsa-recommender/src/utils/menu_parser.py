import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://www.teplitsamenu.ru"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

sections = soup.find_all('div', class_='t030__descr')

menu = {}

for section in sections:
    section_title = section.get_text(strip=True).strip('— ')

    next_section = section.find_next('div', class_='t1025')
    if not next_section:
        continue

    section_dishes = []

    dishes = next_section.find_all('div', class_='t1025__item')

    for dish in dishes:
        name = dish.find('div', class_='t1025__title').get_text(strip=True)

        description_full = dish.find('div', class_='t1025__descr').get_text(strip=True)

        weight_match = re.search(r'(\d+(?:\/\d+)?\s*(?:гр|г)\.?)', description_full)
        weight_info = weight_match.group(0) if weight_match else ""

        composition = re.sub(r'\d+(?:\/\d+)?\s*(?:гр|г)\.?', '', description_full).strip().rstrip(',')

        if not weight_info:
            name_weight_match = re.search(r'(\d+(?:\/\d+)?\s*(?:гр|г)\.?)', name)
            if name_weight_match:
                weight_info = name_weight_match.group(0)
                name = re.sub(r'\d+(?:\/\d+)?\s*(?:гр|г)\.?', '', name).strip()

        price = dish.find('div', class_='t1025__price-value').get_text(strip=True)

        section_dishes.append({
            'name': name,
            'composition': composition,
            'weight_info': weight_info,
            'price': price
        })

    menu[section_title] = section_dishes

with open('menu.json', 'w', encoding='utf-8') as f:
    json.dump(menu, f, ensure_ascii=False, indent=4)

print("Данные успешно сохранены в файл menu.json")
