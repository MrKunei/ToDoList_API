# ToDoList
---

<b>_ToDoList_</b> — планировщик задач, позволяющий работать с целями и отслеживать прогресс в их достижении.
---
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)

---

## Функциональность:

* Вход/регистрация/авторизация через ВК.
* Создание цели.
* Выбор:
  * временные рамки цели с отображением количества дней до достижения цели;
  * категория цели (личная, работа, развитие, спорт и т.д.) с возможностью добавления/удаления/обновления категорий;
  * приоритет цели (статический список второстепенных, основных, критических и т. д.);
  * статус достижения цели (в процессе, выполнено, просрочено, в архиве).
* Редактирование:
  * цели;
  * описание цели;
  * положение дел;
  * приоритет и категория цели.
* Удаление цели.
* При удалении цели ее статус меняется на «в архиве».
* Поиск по названию цели.
* Фильтрация по статусу, категории, приоритету, году.
* Выгрузка целей в CSV/JSON.
* Заметки о целях.

* Телеграм бот:
  * получение списка целей;
  * редактирование целей;
  * создание целей.

---

## Локальный запуск:

  Склонируйте репозиторий.

  Находясь в папке с кодом создайте виртуальное окружение `python -m venv venv`;
  
  Активируйте виртуальное окружение (Windows: `source venv\scripts\activate`; Linux/Mac: `source venv/bin/activate`);

  Установите зависимости `python -m pip install -r requirements.txt`.

  Переименуйте `.env.example` в `.env` и заполните его.

  Для локального запуска, находясь в директории проекта выполните команды:
  ```
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
  ```

## Запуск проекта через Docker

Перейдите в корневую папку проекта где находится файл `docker-compose.yaml` и выполните команду:

```
docker-compose up -d --build
```
