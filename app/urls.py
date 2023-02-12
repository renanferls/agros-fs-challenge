from django.urls import path

from .views import *

urlpatterns = [
    path('producer/', ProducerView.as_view()),
    path('producer/<int:pk>', ProducerView.as_view()),

    path('crop/', CropView.as_view()),
    path('crop/<int:pk>', CropView.as_view()),

    path('crop-report/', CropReportView.as_view()),
    path('crop-report/<int:pk>', CropReportView.as_view()),

]