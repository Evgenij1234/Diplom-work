# Используем Python 3.12
FROM python:3.12.8-slim-bullseye

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Установка Playwright и его зависимостей
RUN pip install --no-cache-dir playwright scrapy scrapy-playwright flask

# Установка браузеров для Playwright
RUN playwright install --with-deps chromium

WORKDIR /parser

COPY . .

# Flask сервер
COPY run_scrapy.py /parser/run_scrapy.py

CMD ["python", "run_scrapy.py"]
