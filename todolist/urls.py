from django.urls import path
from .views import todolistpage

urlpatterns = [
    path('' , todolistpage , name = "todolist"),
]