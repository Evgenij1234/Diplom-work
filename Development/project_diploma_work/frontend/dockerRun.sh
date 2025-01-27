docker-compose stop frontend
docker-compose rm -f frontend
docker rmi frontend
docker-compose build frontend
docker-compose up -d frontend
docker-compose exec frontend /bin/bash