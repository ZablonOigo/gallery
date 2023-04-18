from django.urls import path
from.views import *
app_name='photo'
urlpatterns=[
    path('', index, name='index'),
    path('detail/<int:id>/', view_photo, name='detail'),
    path('create/',create_photo, name='create'),
    path('update/edit/<int:id>/', update_photo, name='edit'),
    path('delete/<int:id>/', delete_photo, name='delete'),
    path('category/search/', search_pic, name='search'),
]