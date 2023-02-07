from django.db import models

from core.models import User


class TgUser(models.Model):
    tg_id = models.BigIntegerField(unique=True)
    tg_chat_id = models.BigIntegerField()
    user = models.ForeignKey(User, models.PROTECT, null=True, blank=True)

    verification_code = models.CharField(max_length=32, null=True, blank=True)