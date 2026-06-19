# Diplom_3

## Автоматизированные UI тесты для веб-приложения Stellar Burgers.

## Реализованные тесты

### Конструктор бургеров

* переход между разделами конструктора
* открытие модальных окон ингредиентов
* закрытие модальных окон
* проверка счётчиков ингредиентов

### Лента заказов (Feed)

* переход в ленту заказов
* проверка отображения списка заказов
* проверка счётчиков «за всё время» и «за сегодня»
* отображение заказов в статусе «в работе»

### Модальные окна

* открытие модального окна ингредиента
* закрытие по клику на крестик
* закрытие по клику на оверлей

## Структура проекта

pages/
locators/
tests/
conftest.py
requirements.txt
README.md

## Запуск тестов

Установка зависимостей:
pip install -r requirements.txt

Запуск всех тестов:
python -m pytest -v

Запуск в Chrome:
python -m pytest -v --browser=chrome

Запуск в Firefox:
python -m pytest -v --browser=firefox

Запуск с Allure

python -m pytest --alluredir=allure-results
allure serve allure-results

## Используемые технологии

pytest
selenium
allure-pytest
webdriver (Chrome / Firefox)
Page Object Model (POM)
