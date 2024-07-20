import pandas as pd
import json

# Пути к файлу Excel и файлу JSON
excel_file_path = "files\Прайс-лист AGC 2024.03.04 Опт.xlsx"
json_file_path = "files\price_list.json"

# Определение через словарь типа машины, в зависимости от каталога
sheets = {
    "Автостекло. Аксессуары. Клей": "Иномарки",
    "Российский автопром": "Отечественные"
}

# Нужные столбцы
required_columns = ["Вид стекла", "Еврокод", "Код AGC", "Старый Код AGC", "Наименование", "ОПТ"]

# Чтение данных из Excel и их обработка
data = []
for sheet_name, catalog in sheets.items():
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name, header=4, usecols=required_columns)
    
    for _, row in df.iterrows():
        price = row["ОПТ"]
        if price == "*": # по заданию - Если у позиции цена фиксированная, то в столбце ОПТ будет *, поэтому такие случаи нужно учесть и в цену ставить Фиксированную цену.
            price = "Фиксированная"
        
        item = {
            "art": row["Код AGC"],
            "eurocode": row["Еврокод"],
            "oldcode": row["Старый Код AGC"],
            "name": row["Наименование"],
            "catalog": catalog,
            "category": row["Вид стекла"],
            "price": price
        }
        data.append(item)

# Запись данных в JSON-файл в папку files
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Данные успешно сохранены в файл {json_file_path}")
