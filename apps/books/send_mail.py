from django.contrib.auth import get_user_model
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

User = get_user_model()


def send_book_activation_email(id, title):
    context = {
        "text": "Hello admin",
        "domain": "http:localhost:8000/",
        "id": id,
        "title": title
    }
    msg_html = render_to_string("activate_book.html", context)
    plain_message = strip_tags(msg_html)
    subject = "Activation Book"
    # to_emails = user.email
    mail.send_mail(
        subject,
        plain_message,
        "rskeldi.official@gmail.com",
        ["rskeldi2015@gmail.com", ],
        html_message=msg_html
    )
