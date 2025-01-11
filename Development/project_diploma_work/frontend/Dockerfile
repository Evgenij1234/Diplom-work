FROM node:18

# Рабочая директория
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package.json package-lock.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем всё приложение
COPY . .

# Открываем порт 3000 для приложения
EXPOSE 3000

# Запуск dev-сервера для разработки (не билд)
CMD ["npm", "start"]
