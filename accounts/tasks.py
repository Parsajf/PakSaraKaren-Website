# from celery import shared_task
# from django.core.mail import send_mail

# @shared_task
# def send_email_task(subject, message, from_email, recipient_list):
#     """
#     A Celery task to send an email asynchronously.

#     Args:
#         subject (str): Subject of the email.
#         message (str): Body of the email.
#         from_email (str): Sender's email address.
#         recipient_list (list): List of recipient email addresses.

#     Returns:
#         int: Number of successfully delivered messages.
#     """
#     return send_mail(subject, message, from_email, recipient_list)