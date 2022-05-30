from django.urls import path
from measurement.views import ListCreateAPIView, RetrieveUpdateAPIView, MeasurementAPIView

urlpatterns = [
    path('sensors/', ListCreateAPIView.as_view()),
    path('sensors/<sensor_id>/', RetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementAPIView.as_view()),
]
