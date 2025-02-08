# parser

./dockerRun.sh - остановк, удаление старого, создание нового образа, запуск, подключение к консоле

# Структура проекта
project_name/
│
├── scrapy.cfg                # Основной файл конфигурации Scrapy
├── project_name/             # Основная директория проекта
│   ├── __init__.py           # Делает директорию Python-пакетом
│   ├── items.py              # Определение данных (Item) для парсинга
│   ├── middlewares.py        # Настройка Middleware (промежуточного ПО)
│   ├── pipelines.py          # Обработка данных перед сохранением
│   ├── settings.py           # Конфигурация проекта
│   └── spiders/              # Директория для пауков
│       ├── __init__.py       # Делает директорию Python-пакетом
│       └── my_spider.py      # Реализация паука (Spider)

# Полезные ссылки
scrapy shell 'url' - парсинг из ссылки
cd catching_materials
scrapy crawl spider_main - запуск паука из файла
