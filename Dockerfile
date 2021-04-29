FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /var/www/html/EDoctor
WORKDIR /var/www/html/EDoctor
ADD . /var/www/html/EDoctor
RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
RUN sed -i 's/\r//' ./remove.sh
RUN chmod +x ./remove.sh
RUN sed -i 's/\r//' ./django.sh
RUN chmod +x ./django.sh
RUN sed -i 's/\r//' ./vue.sh
RUN chmod +x ./vue.sh
RUN sed -i 's/\r//' ./start.sh
RUN chmod +x ./start.sh
RUN sed -i 's/\r//' ./migration.sh
RUN chmod +x ./migration.sh