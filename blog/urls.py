from django.urls import path
from .views import bloglandpage , allposts , blogdetail

urlpatterns = [
    path('' , bloglandpage , name="blogHomePage"),
    path('allposts' ,allposts , name="allposts" ),
    path('blogdetail/<postid>' , blogdetail , name="detail")
]