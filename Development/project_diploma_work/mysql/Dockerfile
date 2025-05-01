FROM mysql:8.0

# Установка переменных окружения
ENV MYSQL_ROOT_PASSWORD=rootpass
ENV MYSQL_DATABASE=appdb
ENV MYSQL_USER=appuser
ENV MYSQL_PASSWORD=userpass

# Открываем порт MySQL
EXPOSE 3306

# Команда запуска MySQL сервера
CMD ["mysqld"]