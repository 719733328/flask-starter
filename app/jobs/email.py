from app.extensions import celery


@celery.task()
def send_welcome_email(to):
    pass
