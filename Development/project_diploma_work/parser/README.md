# parser
 docker build -t parser . СБорка
 docker run -d --name parser -p 3000:3000 parsers
 docker stop parser Остановка
 docker rm parser
 docker start parser Старт собраного
 docker logs parser ПРосмотр логов

 docker attach parser 