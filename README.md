# Лабораторная работа №4

## Построение и конфигурирование системы непрерывной интеграции

Проект использует Python и GitLab CI/CD.

## Этапы Pipeline

1. Check — проверка синтаксиса Python.
2. Test — запуск автоматических тестов.
3. Build — сборка проекта и создание артефактов.
4. Publish — публикация артефактов.

## Запуск локально

Создание виртуального окружения:

python3 -m venv venv

Активация:

source venv/bin/activate

Установка зависимостей:

pip install -r requirements.txt

Запуск:

python main.py

Тестирование:

pytest -v

## GitLab CI/CD

После отправки проекта в GitLab файл .gitlab-ci.yml автоматически
запускает Pipeline.

Pipeline выполняет следующие этапы:

Check -> Test -> Build -> Publish
