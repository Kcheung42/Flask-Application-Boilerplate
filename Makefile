docker-build:
	docker-compose -f docker-compose.yml build

docker-up:
	docker-compose -f docker-compose.yml up -d

ssh-flask:
	docker exec -ti flask_server bash

