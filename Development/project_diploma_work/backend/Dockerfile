FROM php:8.2-apache

# Установка MySQL-драйвера
RUN docker-php-ext-install mysqli

# Копирование PHP-кода в Apache директорию
COPY index.php /var/www/html/

# Права доступа
RUN chown -R www-data:www-data /var/www/html

# Переменные окружения (если нужно)
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
