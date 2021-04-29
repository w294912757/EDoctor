#!/bin/sh
python manage.py collectstatic&&
uwsgi  --ini /var/www/html/EDoctor/uwsgi.ini