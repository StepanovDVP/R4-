from django.urls import path

from .views import SubmitRequestView

urlpatterns = [
    path('', SubmitRequestView.as_view(), name='order_request'),
    path('order-success/', SubmitRequestView.as_view(), name='order_success'),
]
