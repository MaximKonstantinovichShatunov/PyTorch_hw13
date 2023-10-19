import os
import json


STATISTICS_EMPTY = {'win': 0, 'lost': 0, 'lastgame': None}

def load_static(file_name = 'statistics.json'):
    """Функция загрузки информации о статистике пользователя

    - Возвращает статистику побед, поражений и последней игры пользователя, если он не новый 
    - Возвращает пустой словарь, в случае, если пользователь еще не играл"""

    if os.path.exists(file_name):
            with open(file_name, "r", ) as r:
                data = json.load(r)
                print(data)
                return data
    else:
        return {}

def save_users_to_json(users_data: dict, file_name= 'zayavki.json'):
    """Функция сохраняет прогресс пользователя по победам, поражениям и последней игры
    
    - Принимает словарь со значениями побед, поражений и последней игры
    - Записывает в файл statistics.json изменения"""
    with open(file_name, 'a') as file:
        json.dump(users_data, file, indent=4)



def add_user_to_json(users_data: dict, file_name= 'zayavki.json'):
    with open(file_name, 'a') as file:
        data = json.load(file)  # Загрузка данных из файла
        data.append(users_data)  # Добавление нового пользователя в список данных
        file.seek(0)            # Перемещение в начало файла
        json.dump(data, file, indent=4)  # Сохранение обновленных данных в файл