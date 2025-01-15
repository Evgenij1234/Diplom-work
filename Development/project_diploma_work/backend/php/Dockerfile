# Базовый образ PHP с FPM
FROM php:8.2-fpm

# Установка необходимых зависимостей
RUN apt-get update && apt-get install -y \
    zip unzip curl git && \
    docker-php-ext-install pdo pdo_mysql

# Установка Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

# Настройка рабочей директории
WORKDIR /var/www/html

# Копирование проекта Laravel в контейнер
COPY ./laravel/ /var/www/html/

# Установка зависимостей Laravel с помощью Composer
RUN composer install --no-dev --optimize-autoloader

# Генерация APP_KEY для Laravel
RUN php artisan key:generate

# Настройка прав на директории для Laravel
RUN chown -R www-data:www-data /var/www/html/storage /var/www/html/bootstrap/cache

# Открытие порта для PHP-FPM
EXPOSE 8000

# Запуск PHP-FPM
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]
