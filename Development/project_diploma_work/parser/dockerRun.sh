docker-compose stop parser
docker-compose rm -f parser
docker rmi parser
docker-compose build parser
docker-compose up -d parser
docker-compose exec parser /bin/bash