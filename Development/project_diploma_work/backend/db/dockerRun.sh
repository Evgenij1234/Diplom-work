docker-compose stop db
docker-compose rm -f db
docker rmi db
docker-compose build db
docker-compose up -d db
docker-compose exec db /bin/bash