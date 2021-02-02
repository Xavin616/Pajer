web: gunicorn Pajer.wsgi
worker: celery -A Pajer worker --loglevel=info
scheduler: celery -A Pajer beat --loglevel=info