# Базовый образ MySQL
FROM mysql:8

# Копирование SQL скриптов
COPY ./init.sql /docker-entrypoint-initdb.d/init.sql
COPY ./updates/ /docker-entrypoint-initdb.d/updates/

# Установка переменных окружения
ENV MYSQL_ROOT_PASSWORD=ggghosttt123321
ENV MYSQL_DATABASE=parser
ENV MYSQL_USER=evgen
ENV MYSQL_PASSWORD=ggghosttt123321

# Открытие порта MySQL
EXPOSE 3306
