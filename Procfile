web: gunicorn django_hosted_on_heroku_test.wsg:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate