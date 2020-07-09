from app import create_app
import os
flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')
from app.extensions import celery

"""
celery -A run_celery.celery worker  --loglevel=info
"""
