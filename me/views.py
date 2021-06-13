from django.shortcuts import render
from django.http import HttpResponse
from .models import favmovie, favmusic, skills
# Create your views here.

def homePage(request):
    return render(request , 'me/home.html')

def infoPage(request):
    tit = skills.objects.all()
    movie = favmovie.objects.all()
    book = favmusic.objects.all()
    arg = {'topic' : tit , 'movie' : movie , 'book' : book}

    return render(request , 'me/info.html' , arg)