# Используем официальный образ Node.js 22
FROM node:22

# Устанавливаем рабочую директорию внутри контейнера в папку frontend
WORKDIR /frontend

# Копируем файлы package.json и package-lock.json из папки frontend в контейнер
COPY /package*.json ./

# Устанавливаем зависимости
RUN npm install

# Открываем порт 3000 (если ваш React-приложение использует этот порт по умолчанию)
EXPOSE 3000

# ===== РАСКОММЕНТИРУЙТЕ НУЖНУЮ СТРОКУ =====
# Для PROD (использует существующий билд):
##COPY ./build/. ./
##CMD ["npx", "serve", "-s", ".", "-l", "3000"]
    
# Для DEV (исходники + hot-reload):
COPY . .
CMD ["npm", "start"]
