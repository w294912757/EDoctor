#!/bin/sh
git pull&&
docker build -t edoctor_django .&&
docker run -it --name EDoctor_django -p 80:8000 -d edoctor_django&&
sudo docker exec -it EDoctor_django /bin/bash start.sh