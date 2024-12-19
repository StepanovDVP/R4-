from django.db import models

from constants import MAX_LEN_MODEL, MAX_LEN_VERSION, MAX_LEN_SERIAL


class Robot(models.Model):
    serial = models.CharField(
        max_length=MAX_LEN_SERIAL, blank=False, null=False
    )
    model = models.CharField(max_length=MAX_LEN_MODEL, blank=False, null=False)
    version = models.CharField(
        max_length=MAX_LEN_VERSION, blank=False, null=False
    )
    created = models.DateTimeField(blank=False, null=False)
