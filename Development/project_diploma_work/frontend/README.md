# frontend

 docker build -t frontend . СБорка
 docker run -d --name frontend -p 3000:3000 frontend
 docker stop frontend Остановка
 docker rm frontend
 docker start frontend Старт собраного
 docker logs frontend ПРосмотр логов

 docker attach frontend 

