from django.urls import path
from .views import homePage , infoPage

urlpatterns = [
    path('' , homePage , name='home'),
    path('info' , infoPage , name='info'),
]