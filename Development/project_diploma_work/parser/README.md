# parser
# Чтобы установить Scrapy в системах Ubuntu (или на базе Ubuntu), вам необходимо установить следующие зависимости:* 
1. sudo apt -y install python3-pip
2. sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

# Билдим докер для скрапи
docker build -t parser .
# Запускае докер для скрапи
docker run --rm parser
# Подключение докера в качестве рабочей среды через vc code
плагин для работы с dev контейнерами — Dev Containers
В левом нижнем углу кнопки и потом Reopen in Container далее From Dockerfile


