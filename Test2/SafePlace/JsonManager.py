import json
import os

# --- Ввод данных разработчика ---
developer_name = input("Введите имя разработчика: ")
logo_name = "logo.png"

# --- Ввод социальных сетей ---
socials = []
while True:
    icon = input("Введите иконку социальной сети (оставьте пустым, чтобы закончить): ")
    if not icon.strip():
        break
    url = input("Введите URL социальной сети: ")
    socials.append({"icon": icon, "url": url})

# --- Сканирование папок для игр ---
games = []
current_dir = os.getcwd()
for item in os.listdir(current_dir):
    if os.path.isdir(item):
        games.append({
            "title": item,
            "cover": "background.png",
            "link": f"/{item}/"
        })

# --- Создание структуры JSON ---
data = {
    "developer": {
        "name": developer_name,
        "logo": logo_name
    },
    "socials": socials,
    "games": games
}

# --- Сохранение в файл ---
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("JSON файл успешно создан: data.json")
