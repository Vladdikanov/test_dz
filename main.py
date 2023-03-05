from unittest import TestCase
import pytest
import requests
from for_connect import host, headers, OAuth
from selenium import webdriver
import time
print("Задача №1")
print()
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
filter_geo_logs = []
for visit_dict in geo_logs:
    for visit in visit_dict.values():
        if "Россия" in visit:
            filter_geo_logs.append(visit_dict)

print("Задача №2")
print()
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
list_1 =[]
for value in ids.values():
  list_1.extend(value)
unique_list = set(list_1)
print(list(unique_list))
print()

print("Задача №3")
print()
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
len_queries_list = len(queries)
len_queries = [len(q.split()) for q in queries]
len_set = set(len_queries)
dict_word = {}
for l in len_set:
    dict_word[l] = round((len_queries.count(l) / len_queries_list * 100),2)
    print(f"Запрос из {l} слов(а) составляет {len_queries.count(l) / len_queries_list * 100}% из всех запросов")
print(dict_word)


# OAuth = "y0_AgAAAABUoZJXAADLWwAAAADU7U1xmZQbroCkSvunuwTb1x2AtyGspxg"
# headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {OAuth}'}
# host = 'https://cloud-api.yandex.net/v1/disk'
def status_connect():
    res = requests.get(f"{host}", headers=headers)
    if res.status_code == 200:
        print("Подключение успешно")
    else:
        print("Подключение не удалось")
    status = res.status_code

    return status

def create_folder(name_folder):
    params = {"path": name_folder}
    res = requests.put(f"{host}/resources", headers=headers, params= params)
    if res.status_code == 201:
        print(f"Папка {name_folder} успешно создана")
    elif res.status_code == 409:
        print(f"Папка {name_folder} уже существует")
    else:
        print("Не удалось создать папку")
    status = res.status_code

    return status

def get_info(name_folder):
    params = {"path": name_folder}
    res = requests.get(f"{host}/resources", headers=headers, params=params)
    if res.status_code == 200:
        print("Папка присутствует на диске на диске")
    else:
        print("Этой папки нет в списке")
    status = res.status_code

    return status
# url = "https://passport.yandex.ru/auth/"
# driver = webdriver.Chrome(executable_path=r"C:\Users\79130\Desktop\Python_DZ\Test_DZ\chromedriver\chromedriver.exe")
# try:
#     driver.get(url=url)
#     time.sleep(1)
#     email_button = driver.find_elements(by="class",value="AuthLoginInputToggle-type")
#     print(list(email_button))
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()
