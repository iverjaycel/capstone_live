web gunicorn --bind 0.0.0.0:4500 capstone.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
