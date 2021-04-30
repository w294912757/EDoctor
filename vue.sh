#!/bin/sh
git pull&&
cd frontend&&
docker build -t edoctor_vue .&&
docker run -it --name EDoctor_vue -p 800:800 -d edoctor_vue&&
cd ..