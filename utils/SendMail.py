from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


class SendEmail():
    def __init__(self, template, subject, context, to) -> None:
        self.context = context
        self.subject = subject
        self.template = render_to_string(template, self.context)
        self.text_content = strip_tags(self.template)
        self.to = to

    def send(self):
        print(self.to)
        msg = EmailMultiAlternatives(self.subject, self.text_content, 'Dont Reply <support@JobHunt.ng>', [self.to,])
        msg.attach_alternative(self.template, "text/html")
        msg.send()
