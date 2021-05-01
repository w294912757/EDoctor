#!/bin/sh
git pull&&
cd frontend&&
docker build -t edoctor_vue .&&
docker run -it --name EDoctor_vue -p 80:80 -d edoctor_vue&&
cd ..&&
sudo docker exec -it EDoctor_django /bin/bash start.sh