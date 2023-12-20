<div align="center">
  <h3 align="center">Продуктовый помощник Foodgram</h3>
  <p align="center">
    дипломный проект студентки 67 когорты Яндекс.Практикум 2023 г. Карловой Нины.
    <br />
  </p>
</div>

## Описание

«Продуктовый помощник» - это приложение, в котором пользователи могут публиковать рецепты кулинарных изделий, подписываться на публикации других авторов и добавлять рецепты в свое избранное. Сервис «Список покупок» позволит пользователю создавать список продуктов, которые нужно купить для приготовления выбранных блюд согласно рецепта/ов.

Проект доступен по этому [адресу](https://foodgram-nk.hopto.org)

Админка доступна по этому [адресу](https://foodgram-nk.hopto.org/admin/)

## Запуск проекта на локальной машине:

Установить Docker, Docker Compose (для Windows - актуальный Docker Desktop).

1. Клонировать репозиторий:
   ```sh
   git clone https://github.com/Nina2301/foodgram-project-react.git
   ```

2. В директории infra создать файл .env и заполнить своими данными по аналогии с example.env:
```
DB_ENGINE=django.db.backends.postgresql
POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
ALLOWED_HOSTS=127.0.0.1, localhost, backend
SECRET_KEY='секретный ключ Django'
```

3. Из папки infra cоздать и запустить контейнеры Docker, последовательно выполнить команды по созданию миграций, сбору статики, 
созданию суперпользователя:
   ```sh
   docker compose up -d --build
   ```
   ```sh
   docker compose exec backend python manage.py makemigrations
   ```
   ```sh
   docker compose exec backend python manage.py migrate
   ```
   ```sh
   docker compose exec backend python manage.py createsuperuser
   ```
   ```sh
   docker compose exec backend python manage.py collectstatic --noinput
   ```

4. Наполнить базу данных содержимым из файла ingredients.json:
  ```
  docker-compose exec backend python manage.py load_ingredients
  ```


После запуска проект будет доступен по адресу: [http://127.0.0.1/](http://127.0.0.1/)

Документация будет доступна по адресу: [http://127.0.0.1/api/docs/](http://127.0.0.1/api/docs/)

## Развернуть проект на удаленном сервере:

1. Клонировать репозиторий:
   ```sh
   git clone https://github.com/Nina2301/foodgram-project-react.git
   ```

2. Установить Docker Compose на сервер:
  ```
  sudo apt update
  sudo apt install curl
  curl -fSL https://get.docker.com -o get-docker.sh
  sudo sh ./get-docker.sh
  sudo apt install docker-compose-plugin
  ```
3. Скопировать со своего компьютера из папки infra на сервер в директорию infra/ файл docker-compose.production.yml:
  ```
  scp -i path_to_SSH/SSH_name docker-compose.production.yml \
    username@server_ip:/home/username/foodgram/infra/docker-compose.production.yml
  ```
  ```
  (username - имя пользователя на сервере, IP - публичный IP сервера)
  ```

4. Скопировать со своего компьютера из папки infra на сервер в директорию infra/ файл .env:
  ```
  scp -i path_to_SSH/SSH_name .env \
    username@server_ip:/home/username/foodgram/infra/.env
  ```

5. На сервере из папки infra cоздать и запустить контейнеры Docker, последовательно выполнить команды по созданию миграций, 
сбору статики, созданию суперпользователя:
   ```sh
   sudo docker compose -f docker-compose.production.yml up -d
   ```
   ```sh
   sudo docker compose -f docker-compose.production.yml exec backend python manage.py makemigrations
   ```
   ```sh
   sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
   ```
   ```sh
   sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic --no-input
   ```
   ```sh
   sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
   ```

6. Наполнить базу данных содержимым из файла ingredients.json:
  ```
    sudo docker compose -f docker-compose.production.yml exec backend python manage.py load_ingredients
  ```

На этом всё, продуктовый помощник запущен на вашем удаленном сервере, можно наполнять его рецептами и делиться с друзьями!

## Авторы

Яндекс Практикум

Нина Карлова 67 когорта nina-karlova@yandex.ru
