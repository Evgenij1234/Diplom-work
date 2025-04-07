#!/bin/bash

# Запускаем Redis в фоне
redis-server --appendonly yes &

# Ожидаем запуска Redis
sleep 2

# Основной процесс (может быть пустым, так как парсер будет запускаться по команде)
tail -f /dev/null