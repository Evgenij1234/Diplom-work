# parser
FROM python:3.12.8-slim-bullseye
RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*
COPY parser/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /parser
COPY parser/ .
CMD ["python", "parser.py"]

# apache

# backend

# db

# frontend


