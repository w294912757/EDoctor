#!/bin/bash
docker rm -f EDoctor_django&&
docker rm -f EDoctor_vue&&
docker rmi -f edoctor_django&&
docker rmi -f edoctor_vue&&
git pull&&
docker build -t edoctor_django .&&
docker run -it --name EDoctor_django -p 8020:8020 -d edoctor_django&&
docker exec -it EDoctor_django /bin/bash&&
python manage.py makemigrations&&
python manage.py migrate&&
uwsgi   --enable-threads /var/www/html/EDoctor/uwsgi.ini&&
exit&&
docker build -t edoctor_vue .&&
docker run -it --name EDoctor_vue -p 80:80 -d edoctor_vue&&