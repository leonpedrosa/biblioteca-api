from celery import shared_task, states


@shared_task
def forgot_send_email(user_id=None):
    print('Enviando email')
    return