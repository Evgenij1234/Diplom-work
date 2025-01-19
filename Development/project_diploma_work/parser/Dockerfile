# parser
FROM python:3.12.8-slim-bullseye

# Установка зависимостей
RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Установка Flask
RUN pip install flask

# Установка рабочей директории
WORKDIR /parser

# Копирование файлов проекта
COPY . .

# Создание простого Flask сервера
COPY run_scrapy.py /parser/run_scrapy.py

# Запуск сервера Flask
CMD ["python", "run_scrapy.py"]

