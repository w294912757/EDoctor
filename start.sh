#!/bin/bash
python manage.py makemigrations&&
python manage.py migrate&&
uwsgi   --enable-threads /var/www/html/api_automation_test/uwsgi.ini