# OS 
Linux Ubuntu 24.04.1 LTS

# Порты
3000 Фронт
8000 Бэк
5000 Парсер

# Доп ПО
1. Docker 
2. Docker-Compose
3. vim  

sudo systemctl start docker
# Команды для сборки всего проекта
docker-compose down - вырубить все
docker-compose up --build - собрать и запустить
docker-compose up -d - запустить все
docker-compose build СОбрать все
docker-compose build --no-cache - собрать с нуля все

# Включить/выключить определенный контейнер
docker-compose stop parser
docker-compose start parser

# очистка
docker-compose down --volumes --remove-orphans
docker system prune -a

# Удаление кэша
docker builder prune -a
docker system prune -a -f

# Удаляем ВМ и все данные (это очистит всё!)
rm -rf ~/.docker/desktop/vms/0/data/Docker.raw