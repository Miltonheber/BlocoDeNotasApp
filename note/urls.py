from django.urls import path
from .views import *


urlpatterns = [
    path('', homecreate, name='home'),
    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:id>', updatenote, name='update'),
    path('listall', listall, name='listall'),
]
