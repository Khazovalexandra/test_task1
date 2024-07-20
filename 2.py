import json
import pandas as pd

# Путь к JSON файлу с каталогом и к выходному Excel файлу
json_file_path = "files\price_list.json"
output_excel_file_path = "files\client_catalog.xlsx"

# Нужные категории
categories_needed = ["ветровое", "заднее", "боковое"]

# Чтение данных из JSON файла
with open(json_file_path, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Фильтрация и расчет цен для клиента
client_data = []

for item in data:
    if item["category"] in categories_needed:
        price = item["price"]
        if price == "Фиксированная":
            client_price = "Фиксированная"
        else:
            if item["category"] == "ветровое":
                client_price = (price + 1000) * 1.05
            elif item["category"] == "заднее":
                client_price = (price + 800) * 1.07
            elif item["category"] == "боковое":
                client_price = price * 1.10

        client_item = {
            "catalog": item["catalog"],
            "category": item["category"],
            "art": item["art"],
            "eurocode": item["eurocode"],
            "oldcode": item["oldcode"],
            "name": item["name"],
            "client_price": client_price
        }
        client_data.append(client_item)

# Создание DataFrame и запись в Excel
client_df = pd.DataFrame(client_data)

client_df.to_excel(output_excel_file_path, index=False, sheet_name='Каталог товаров')

print(f"Каталог для клиента успешно сохранен в файл {output_excel_file_path}")
