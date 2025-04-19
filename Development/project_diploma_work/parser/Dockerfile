# Базовый образ Python с Redis
FROM python:3.12.8-slim-bullseye

# Установка Redis
RUN apt-get update && \
    apt-get install -y redis-server && \
    rm -rf /var/lib/apt/lists/*

# Установка зависимостей для парсера
RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libatspi2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libxkbcommon0 \
    libasound2 \
    libcups2 \
    libpango-1.0-0 \
    libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# Установка зависимостей Python из requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Установка chromium через playwright
RUN playwright install chromium

# Установка рабочей директории
WORKDIR /parser

# Копирование файлов проекта в контейнер
COPY . .

# Экспонирование порта для Flask
EXPOSE 5000

# Команда для запуска приложения Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
