# OS Linux Ubuntu 24.04.1 LTS

# Доп ПО
1. Docker, 
2. Docker-Compose
3. vim  

# Команды для сборки всего проекта
docker-compose up --build
docker-compose build
docker-compose build --no-cache

# Подключение докера в качестве рабочей среды через vc code
1. плагин для работы с dev контейнерами — Dev Containers
2. Запустить контейнер
3. В левом нижнем углу кнопки и потом "Reopen in Container", выбрать первый вариант из предложенных(из рабочей области докера) далее "From Dockerfile"

ПРосмотр логов отдельного сервиса
docker-compose logs \dir\

# очистка
docker-compose down --volumes --remove-orphans
docker system prune -a


