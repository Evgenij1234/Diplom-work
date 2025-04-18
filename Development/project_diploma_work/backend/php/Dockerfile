FROM php:8.3-fpm

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    git unzip libzip-dev libpq-dev \
    && docker-php-ext-install pdo pdo_mysql zip

# Копируем весь проект
COPY ./api /var/www/html
WORKDIR /var/www/html

# Установка Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Установка зависимостей проекта (включая Doctrine)
RUN composer install --optimize-autoloader --no-dev \
    && composer require symfony/orm-pack doctrine/doctrine-bundle

# Права на папку var
RUN chown -R www-data:www-data var

# Запуск Symfony (если используешь Symfony CLI)
CMD ["symfony", "server:start", "--no-tls"]
