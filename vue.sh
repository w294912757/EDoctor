#!/bin/sh
git pull&&
cd frontend&&
npm install&&
npm run build&&
docker build -t edoctor_vue .&&
docker run -it --name EDoctor_vue -p 80:80 -d edoctor_vue