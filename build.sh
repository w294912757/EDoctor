#!/bin/bash
git pull&&
cd frontend&&
docker build -t edoctor_vue .&&
docker run -it --name EDoctor_vue -p 80:80 -d edoctor_vue&&
cd ..&&
docker build -t edoctor_django .&&
docker run -it --name EDoctor_django -p 8020:8020 -d edoctor_django&&
docker exec -it EDoctor_django /bin/bash
