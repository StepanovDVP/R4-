from constants import REQUEST_WAIT_LIST, ROBOT_EXIST
from customers.models import Customer
from robots.models import Robot

from .models import Order, WaitList


class OrderService:
    @staticmethod
    def process_order(email, model, version):
        robot_serial = f'{model.upper()}-{version.upper()}'
        customer, _ = Customer.objects.get_or_create(email=email)
        robot_exist = Robot.objects.filter(
            serial=robot_serial
        ).exists()

        if not robot_exist:
            WaitList.objects.create(
                customer=customer, robot_serial=robot_serial
            )
            return REQUEST_WAIT_LIST

        Order.objects.create(
            customer=customer, robot_serial=robot_serial
        )
        return ROBOT_EXIST
