from django.urls import path, include
from .views import CoreView


app_name = 'web-root'

urlpatterns = [
    path('',CoreView.as_view(), name='core'),
]