python manage.py makemigrations&&
python manage.py migrate&&
uwsgi   --enable-threads /var/www/html/EDoctor/uwsgi.ini&&
exit