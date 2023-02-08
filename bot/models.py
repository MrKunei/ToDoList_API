import os
from django.db import models
from core.models import User



class TgUser(models.Model):
    tg_id = models.BigIntegerField(unique=True)
    tg_chat_id = models.BigIntegerField()
    username = models.CharField(max_length=255, null=True, blank=True, default=None)
    user = models.ForeignKey(User, models.PROTECT, null=True, blank=True, default=None)


    verification_code = models.CharField(max_length=32, null=True, blank=True, default=None)

    def set_verification_code(self):
        code = os.urandom(12).hex()
        self.verification_code = code