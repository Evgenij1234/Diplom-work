# Базовый образ PHP с FPM
FROM php:8.2-fpm

# Установка необходимых зависимостей
RUN apt-get update && apt-get install -y \
    zip unzip curl git libxml2-dev && \
    docker-php-ext-install pdo pdo_mysql xml

RUN apt-get update && apt-get install -y \
    libpng-dev libjpeg-dev libfreetype6-dev && \
    docker-php-ext-configure gd --with-freetype --with-jpeg && \
    docker-php-ext-install gd

# Установка Composer
COPY --from=composer:2.6 /usr/bin/composer /usr/bin/composer

# Настройка рабочей директории
WORKDIR /var/www/html

# Копирование файлов проекта в контейнер
COPY ./my_project_directory/ /var/www/html/

# Установка зависимостей Symfony
RUN composer install --optimize-autoloader

# Установка прав для доступа к кешу и логам
RUN chown -R www-data:www-data /var/www/html/var && \
    chmod -R 775 /var/www/html/var

# Открытие порта для приложения
EXPOSE 8000

# Запуск PHP-FPM
CMD ["php-fpm"]
