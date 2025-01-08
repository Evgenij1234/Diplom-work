# Python образ
FROM python:3.12.8-slim-bullseye

# Устанавливаем системные зависимости
RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем рабочую директорию
WORKDIR /parser

# Копируем все файлы проекта в рабочую директорию контейнера
COPY . .

# Указываем команду для запуска приложения
CMD ["python", "parser.py"]