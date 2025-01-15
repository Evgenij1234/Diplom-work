#!/bin/bash

# Выполнение миграций
php artisan migrate --force

# Запуск PHP-сервера
php artisan serve --host=0.0.0.0 --port=8000
