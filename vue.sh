#!/bin/sh
cd frontend&&
docker build -t edoctor_vue .&&
docker run -it --name EDoctor_vue -p 80:80 -d edoctor_vue&&
docker exec -it EDoctor_vue /bin/bash