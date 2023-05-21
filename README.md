docker-compose build 

docker-compose run --rm SoundUNder_search_ms app -c "python manage.py makemigrations"

docker-compose run --rm SoundUNder_search_ms app -c "python manage.py migrate"

para crear superusuario django:
docker-compose run --rm SoundUNder_search_ms app -c "pythonmanage.py createsuperuser" 

docker-compose up

[local]
Para consultar la documentación:

127.0.0.1:8000/api/docs/

Para búsqueda: 

127.0.0.1:8000/search_ms/songs?search=

Para búsqueda por id dando lista de id's:

ejemplo:
127.0.0.1:8000/search_ms/songs/?ids=1,2,3