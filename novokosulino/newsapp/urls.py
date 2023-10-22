from django.urls import path
from newsapp.views import *


urlpatterns = [
    path('', index),
    path('tables/', tables),
    path('charts/', charts),
]
