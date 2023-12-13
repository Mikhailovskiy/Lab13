# Роботу розпочав студент Михайловський Олексій
import csv
import json


data = [
    ["Country Name", "Code", "Year", "Life expectancy at birth total (years)"],
    ["Afghanistan", "AFG", 1956, 13.7275],
    ["Afghanistan", "AFG", 1978, 19.7245],
    ["Afghanistan", "AFG", 1990, 20.8275]
]


filename = "output.csv"


with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Дані були записані у файл {filename}")



# Вказуємо імена файлів
csv_filename = "output.csv"
json_filename = "output.json"

try:
    # Відкриваємо CSV-файл для читання
    with open(csv_filename, mode='r') as csv_file:
        # Читаємо дані з CSV
        csv_reader = csv.DictReader(csv_file)

        # Створюємо список для зберігання рядків
        data = []

        # Перетворюємо дані з CSV у список словників
        for row in csv_reader:
            data.append(row)

    # Записуємо дані у JSON-файл
    with open(json_filename, mode='w') as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Дані були переписані з {csv_filename} у {json_filename}")

except FileNotFoundError:
    print(f"Помилка: Файл {csv_filename} не знайдено")

except Exception as e:
    print(f"Виникла помилка: {e}")

    #Боднар Степан
updated_data = [
    {"Country Name": "Ukraine", "Code": "UKR", "Year": 2000, "Life expectancy at birth total (years)": 72.3},
    {"Country Name": "USA", "Code": "USA", "Year": 2005, "Life expectancy at birth total (years)": 77.1}
]
try:
    # Зчитуємо дані з JSON-файлу
    with open(json_filename, mode='r') as json_file:
        # Завантажуємо дані з JSON
        data = json.load(json_file)

    # Оновлюємо дані з новими рядками
    data.extend(updated_data)

    # Відкриваємо CSV-файл для запису (mode='a' для додавання до існуючого файлу)
    with open(csv_filename, mode='a', newline='') as csv_file:
        # Створюємо об'єкт для запису у CSV
        writer = csv.writer(csv_file)

        # Записуємо нові рядки
        for row in updated_data:
            writer.writerow(row.values())

    print(f"Дані були додані та переписані з {json_filename} у {csv_filename}")

except FileNotFoundError:
    print(f"Помилка: Файл {json_filename} не знайдено")

except Exception as e:
    print(f"Виникла помилка: {e}")
    
try:
    # Відкриваємо CSV-файл для читання
    with open(csv_filename, mode='r') as csv_file:
        # Читаємо дані з CSV
        csv_reader = csv.DictReader(csv_file)

        # Створюємо список для зберігання рядків
        data = []

        # Перетворюємо дані з CSV у список словників
        for row in csv_reader:
            data.append(row)

    # Записуємо дані у JSON-файл
    with open(json_filename, mode='w') as json_file:
        json.dump(data, json_file, indent=3)

    print(f"Дані були переписані з {csv_filename} у {json_filename}")

except FileNotFoundError:
    print(f"Помилка: Файл {csv_filename} не знайдено")

except Exception as e:
    print(f"Виникла помилка: {e}")
    #Цю частину виконав Шевченко Вадим.
#Код нижче виконаний Шамраєм Максимом
updated_data = [
    {"Country Name": "Italy", "Code": "IT", "Year": 2001, "Life expectancy at birth total (years)": 69.3},
    {"Country Name": "France", "Code": "FR", "Year": 2002, "Life expectancy at birth total (years)": 74.1}
]
try:
    # Зчитуємо дані з JSON-файлу
    with open(json_filename, mode='r') as json_file:
        # Завантажуємо дані з JSON
        data = json.load(json_file)

    # Оновлюємо дані з новими рядками
    data.extend(updated_data)

    # Відкриваємо CSV-файл для запису (mode='a' для додавання до існуючого файлу)
    with open(csv_filename, mode='a', newline='') as csv_file:
        # Створюємо об'єкт для запису у CSV
        writer = csv.writer(csv_file)

        #Записуємо нові рядки
        for row in updated_data:
            writer.writerow(row.values())

    print(f"Дані були додані та переписані з {json_filename} у {csv_filename}")

except FileNotFoundError:
    print(f"Помилка: Файл {json_filename} не знайдено")

except Exception as e:
    print(f"Виникла помилка: {e}")  
    