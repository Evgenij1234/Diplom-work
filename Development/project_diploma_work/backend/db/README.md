# db

./dockerRun.sh - остановк, удаление старого, создание нового образа, запуск, подключение к консоле

Экспорт данных (из контейнера в локальный файл): 
docker exec mysql-container mysqldump -u parser -pparser parser > ./backend/db/backup.sql

Импорт данных (из локального файла в контейнер):
docker exec -i mysql-container mysql -u parser -pparser parser < ./backend/db/backup.sql






