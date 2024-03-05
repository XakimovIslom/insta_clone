from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max

from common.models import BaseModel
from config.settings.base import AUTH_USER_MODEL


class Message(BaseModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="from_user")
    recipient = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="to_user")
    body = models.TextField(null=True)
    is_read = models.BooleanField(default=False)

    def sender_message(from_user, to_user, body):
        sender_message = Message(
            user=from_user,
            sender=from_user,
            recipient=to_user,
            body=body,
            is_read=True
        )
        sender_message.save()

        recipient_message = Message(
            user=to_user,
            sender=from_user,
            reciepient=from_user,
            body=body,
            is_read=True
        )
        recipient_message.save()
        return sender_message

    # def get_message(user):
    #     users = []
    #     messages = (Message.objects.filter(user=user).values('recipient').annotate(last=Max('created_at'))
    #                 .order_by('-last'))
    #     for message in messages:
    #         users.append({
    #             'user': User.objects.get(pk=message['recipient']),
    #             'last': message['last'],
    #             'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
    #         })
    #     return users
