FROM python:3.7
RUN mkdir -p /var/www/html/backend
WORKDIR /var/www/html/backend
ADD . /var/www/html/backend
RUN pip install https://github.com/darklow/django-suit/tarball/v2
RUN pip install -i https://pypi.doubanio.com/simple uwsgi
RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
RUN sed -i 's/\r//' ./remove.sh
RUN chmod +x ./remove.sh
RUN sed -i 's/\r//' ./django.sh
RUN chmod +x ./django.sh
RUN sed -i 's/\r//' ./vue.sh
RUN chmod +x ./vue.sh
RUN sed -i 's/\r//' ./server.sh
RUN chmod +x ./server.sh
EXPOSE 8020