FROM python:3.7
ENV PYTHONUNBUFFERED 1
COPY pip.conf /root/.pip/pip.conf

RUN mkdir -p /var/www/html/EDoctor
WORKDIR /var/www/html/EDoctor
ADD . /var/www/html/EDoctor
RUN pip install -r requirements.txt
RUN chmod +x ./django.sh
RUN chmod +x ./vue.sh
RUN chmod +x ./rmdjango.sh
RUN chmod +x ./rmvue.sh
RUN chmod +x ./start.sh
RUN chmod +x ./migration.sh
RUN chmod +x ./ip.sh

