from django.contrib import admin
from django.urls import include, path

from robots.views import generate_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('robots.urls')),
    path('download_report/', generate_report, name='download_report'),
    path('', include('orders.urls'))
]
