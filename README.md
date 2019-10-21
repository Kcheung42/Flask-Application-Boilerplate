#  Intro

This is a WIP boilerpalte for developing Flask applications

Current technologies used:

- Container: Docker
- Web Framework: Flask
- ORM: SQLAlchemy
- Database: PostgreSQL


### To Build
```
make docker-build
```

### To Run
```
make docker-up
```

### To Test
```
docker exec -it app python manage.py test
```
