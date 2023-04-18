from django.urls import path
from.views import *

urlpatterns=[
    path('', index, name='index'),
    path('detail/<int:id>/', view_photo, name='detail'),
]