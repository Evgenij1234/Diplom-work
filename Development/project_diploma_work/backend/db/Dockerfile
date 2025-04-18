# Базовый образ MySQL
FROM mysql:8.0

# Копирование SQL скриптов
COPY ./init.sql /docker-entrypoint-initdb.d/init.sql
COPY ./migrations/ /docker-entrypoint-initdb.d/migrations/

# Установка переменных окружения
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=parser
ENV MYSQL_USER=parser
ENV MYSQL_PASSWORD=parser

# Открытие порта MySQL
EXPOSE 3306
