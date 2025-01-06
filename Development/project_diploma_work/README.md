# Описание структуры обязательных папок для докера
project/
├── docker-compose.yml
├── .env
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/  # Исходный код React
├── backend/
│   ├── Dockerfile
│   ├── composer.json
│   └── src/  # Исходный код Laravel
├── parser/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── scraper/  # Исходный код Scrapy
├── db/
│   └── data/  # Для хранения данных MySQL
└── apache/
    └── apache2.conf


# Доп ПО
1. Docker, Docker-Compose
2. vim  <sudo apt install vim>

# Команды

собрать docker-compose build
Запуск контейнеров docker-compose up
Остановка docker-compose down




