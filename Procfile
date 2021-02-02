web: gunicorn Pajer.wsgi
main_worker: celery -A Pajer worker --beat --loglevel=info