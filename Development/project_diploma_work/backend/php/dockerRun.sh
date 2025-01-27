docker-compose stop php
docker-compose rm -f php
docker rmi php
docker-compose build php
docker-compose up -d php
docker-compose exec php /bin/bash