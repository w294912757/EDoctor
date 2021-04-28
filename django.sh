#!/bin/sh
git pull&&
docker build -t edoctor_django .&&
docker run -it --name EDoctor_django -p 8020:8020 -d edoctor_django&&
docker exec -it EDoctor_django /bin/bash
