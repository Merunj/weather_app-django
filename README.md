# WeatherApp

WeatherApp - это погодное приложение, разработанное с использованием Django. Оно позволяет пользователям узнавать текущую погоду в любом городе, используя API Яндекс.Погоды для получения погодных данных. Для получения координат города используется библиотека geopy. Интерфейс приложения разработан с использованием Bootstrap для обеспечения привлекательного дизайна.

## Функциональные возможности

- Поиск погоды по названию города
- Отображение текущей температуры, влажности, скорости ветра и других погодных данных
- Интерфейс, разработанный с использованием Bootstrap

## Технологии

- **Django** - основной фреймворк для разработки приложения
- **geopy** - библиотека для работы с географическими координатами
- **Яндекс.Погода API** - API для получения погодных данных
- **Bootstrap** - CSS фреймворк для разработки адаптивного интерфейса

## Установка

1. Клонируйте репозиторий на локальную машину:
    ```cmd
    https://github.com/Merunj/weather_app-django.git
    ```
2. Перейдите в директорию проекта:
    ```cmd
    cd WeatherApp
    ```
3. Создайте и активируйте виртуальное окружение:
    ```cmd
    python -m venv venv
    venv\Scripts\activate
    ```
4. Установите зависимости:
    ```cmd
    pip install -r requirements.txt
    ```
5. Вставьте ваш API Яндекс.Погода:
    В функции index() в файле views.py в переменную access_key вставить токен, полученный на [Яндекс.Погода](https://yandex.ru/dev/weather/):
    ```python
    access_key = 'YOUR_API_TOKEN'
    ```
6. Примените миграции:
    ```cmd
    python manage.py migrate
    ```
7. Запустите сервер разработки:
    ```cmd
    python manage.py runserver
    ```

## Использование

1. Перейдите в браузере по адресу `http://127.0.0.1:8000/`.
2. Введите название города в поле поиска.
3. Получите текущие погодные данные для выбранного города.

## Тестирование

Для запуска тестов выполните следующую команду:
```cmd
python manage.py test
