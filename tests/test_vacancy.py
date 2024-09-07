import pytest


def test_vacansy_init(vacansy_1):
    """Тестирование инициализации."""
    assert vacansy_1.title == "Инженер"
    assert vacansy_1.link == "artemtim.ru"
    assert vacansy_1.salary == 50000
    assert vacansy_1.area == "Москва"
    assert vacansy_1.description == "Работа с технической документацией"
    assert vacansy_1.requirement == "Опрыт работы от 3 лет. Высшее образование."
    assert (
        str(vacansy_1)
        == "Вакансия - Инженер, зарплата - 50000, местоположение - Москва, ссылка на вакансию - artemtim.ru."
    )


def test_vacansy_comparision(vacansy_1, vacansy_2):
    """Тестирование операций сравнения вакансий по размеру зарплаты."""
    assert vacansy_1.salary < vacansy_2.salary
    assert vacansy_2.salary >= vacansy_1.salary
