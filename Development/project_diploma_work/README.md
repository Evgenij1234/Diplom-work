# OS 
Linux Ubuntu 24.04.1 LTS

# Порты
3000 Фронт
80 Бэк

# Доп ПО
1. Docker, 
2. Docker-Compose
3. vim  
# Команды докера
docker ps
docker ps -a
docker stop <container_name_or_id>
docker rm <container_name_or_id>
docker logs <container_name_or_id>
docker exec -it <container_name_or_id> bash
docker attach <container_name_or_id>

docker build -t parser <path_to_dockerfile_directory> или . если в той же деректории, что и терминалы
docker stop <container_name_or_id>
docker rm <container_id_or_name>
docker run -d --name name -p 3000:3000 my-app
docker start <container_name_or_id>

# Команды для сборки всего проекта
docker-compose down - вырубить все
docker-compose up --build - собрать и запустить
docker-compose up -d - запустить все
docker-compose build СОбрать все

docker-compose build --no-cache - собрать с нуля все

# Подключение к терминалу контейнера 
docker exec -it <name>-container bash



# Подключение докера в качестве рабочей среды через vc code
1. плагин для работы с dev контейнерами — Dev Containers
2. Запустить контейнер
3. В левом нижнем углу кнопки и потом "Reopen in Container", выбрать первый вариант из предложенных(из рабочей области докера) далее "From Dockerfile"

# очистка
docker-compose down --volumes --remove-orphans
docker system prune -a

# Удаление всех контейнеров
docker stop $(docker ps -q)
docker rm $(docker ps -a -q) контейнеры
docker rmi $(docker images -q) образы

# Удаление кэша
docker builder prune -a
docker system prune -a -f

