from django.urls import path
from .views import *


urlpatterns = [
    path('', homeCreate, name='home'),
    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:id>', updateNote, name='update'),
    path('listall', listAll, name='listall'),
]
