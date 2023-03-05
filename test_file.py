import pytest
from for_connect import host, headers, OAuth
from main import filter_geo_logs, unique_list, dict_word, status_connect, create_folder, get_info

@pytest.mark.parametrize("dict",[{'visit1': ['Москва', 'Россия']},
                 {'visit3': ['Владимир', 'Россия']},
                 {'visit7': ['Тула', 'Россия']},
                 {'visit8': ['Тула', 'Россия']},
                 {'visit9': ['Курск', 'Россия']},
                 {'visit10': ['Архангельск', 'Россия']}])
def test_geo_list(dict):

    assert dict in filter_geo_logs
    assert len(filter_geo_logs) == 6


@pytest.mark.parametrize("el",[213, 15, 54, 119, 98, 35])
def test_unique_list(el):
    assert el in unique_list
    assert len(unique_list) == 6
@pytest.mark.parametrize("key, value",[(2, 42.86), (3, 57.14)])
def test_words(key, value):
    assert value == dict_word[key]
def test_connect():
    status = status_connect()
    assert status == 200

def test_create_folder():
    name_folder = "Название папки"
    status = create_folder(name_folder)
    assert status in [201,409,423]
def test_get_info():
    name_folder = "Название папки"
    status = get_info(name_folder)
    assert status in [200,423]


