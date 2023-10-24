from django.urls import path
from newsapp.views import *


urlpatterns = [
    path('', index, name='home'),
    path('tables/', tables, name='tables'),
    path('charts/', charts, name='charts'),
    path('charts-test/', charts_test, name='charts-test'),
]
