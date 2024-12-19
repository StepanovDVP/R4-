from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from R4C.settings import DEFAULT_FROM_EMAIL, ROBOT_NOTIFICATION_MESSAGE
from robots.models import Robot

from .forms import OrderForm
from .models import Order, WaitList
from .services import OrderService


class SubmitRequestView(FormView):
    template_name = 'order_form.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_success')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        model = form.cleaned_data['model']
        version = form.cleaned_data['version']
        message = OrderService.process_order(email, model, version)
        return render(
            self.request, 'order_success.html',
            {'message': message}
        )


@receiver(post_save, sender=Robot)
def process_waitlist(sender, instance, created, **kwargs):
    """
    Проверить лист ожидания на наличие добавленного робота.
    В случае успеха добавить заказ в Order и обновить WaitList.
    """
    if created:
        robot_serial = instance.serial
        waitlist_entries = WaitList.objects.filter(
            robot_serial=robot_serial
        ).select_related('customer').order_by(
            'created_at'
        )

        for entry in waitlist_entries:
            Order.objects.create(
                customer=entry.customer, robot_serial=robot_serial
            )
            send_notification_to_customer(entry.customer.email, instance)
            entry.delete()


def send_notification_to_customer(email, robot):
    """Отправить сообщение пользователю."""
    message = ROBOT_NOTIFICATION_MESSAGE.format(
        model=robot.model, version=robot.version
    )
    send_mail(
        subject='Robot available!',
        message=message,
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=True,
    )
