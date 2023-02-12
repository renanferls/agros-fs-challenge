from django.urls import path

from .views import *

urlpatterns = [
    path('producer/', ProducerListCreate.as_view()),
    path('producer/<int:pk>/', ProducerReadUpdateDelete.as_view()),

    path('crop/', CropListCreate.as_view()),
    path('crop/<int:pk>/', CropReadUpdateDelete.as_view()),

    path('crop-report/', CropReportListCreate.as_view()),
    path('crop-report/<int:pk>/', CropReportReadUpdateDelete.as_view()),

    path('search-reports/', SearchReports.as_view()),
]