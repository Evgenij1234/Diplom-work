# Используем официальный образ с PHP
FROM php:8.0-apache

# Устанавливаем расширение для работы с MySQL
RUN docker-php-ext-install mysqli

# Копируем наш код в контейнер
COPY index.php /var/www/html/

# Открываем порт 80
EXPOSE 80
