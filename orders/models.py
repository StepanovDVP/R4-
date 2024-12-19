from django.db import models

from constants import MAX_LEN_SERIAL
from customers.models import Customer


class BaseOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot_serial = models.CharField(
        max_length=MAX_LEN_SERIAL, blank=False, null=False
    )

    class Meta:
        abstract = True


class Order(BaseOrder):
    pass


class WaitList(BaseOrder):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
