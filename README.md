# Проект Game_tg_bot_candies

[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)

## Описание

Проект "Game_tg_bot_candies" игровой телеграм бот. Игроки по очереди берут конфеты, побеждает тот, кто делает последний ход.

Бот в процессе игры ведет подсчет количества конфет, которые необходимо взять при каждом ходе для безоговорочной победы.

## Как запустить проект локально:

Клонировать репозиторий и перейти в него в командной строке:

``` git@github.com:VictorTsyganov/Game_tg_bot_candies.git ```

Создать и активировать виртуальное окружение:

``` python -m venv venv ``` 

* Если у вас Linux/macOS:
    ``` source venv/bin/activate ``` 

* Если у вас Windows:
    ``` source venv/Scripts/activate ```
    
``` python -m pip install --upgrade pip ``` 

Перейти в папку Game_tg_bot_candies в командной строке:

``` cd Game_tg_bot_candies ``` 

Установить зависимости из файла requirements:

``` pip install -r requirements.txt ``` 

Заполнить токен вашего telegtam бота в create.py

Запустить программу:

``` python main.py ```

## Системные требования
- Python 3.9+
- Works on Linux, Windows, macOS

## Стек технологий

- Python 3.9

- aiogram 2.24

## Автор

[Виктор Цыганов](https://github.com/VictorTsyganov)