# Используем официальный образ с PHP
FROM php:8.0-apache

WORKDIR /backend
# Устанавливаем расширение для работы с MySQL
RUN docker-php-ext-install mysqli

COPY . .
# Копируем наш код в контейнер
COPY index.php /var/www/html/

# Открываем порт 80
EXPOSE 80
