FROM python:3.7
RUN mkdir -p /var/www/html/EDoctor
WORKDIR /var/www/html/EDoctor
ADD . /var/www/html/EDoctor
RUN pip install https://github.com/darklow/django-suit/tarball/v2
RUN pip install -i https://pypi.doubanio.com/simple uwsgi
RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
RUN sed -i 's/\r//' ./remove.sh
RUN chmod +x ./remove.sh
RUN sed -i 's/\r//' ./build.sh
RUN chmod +x ./build.sh
RUN sed -i 's/\r//' ./server.sh
RUN chmod +x ./server.sh