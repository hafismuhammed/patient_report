from django.urls import path
from .views import ClinicReportView


urlpatterns = [
    path('clinic-report/', ClinicReportView.as_view(), name='Clinic Report')
]
