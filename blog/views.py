from django.shortcuts import render
from django.http import HttpResponse
from .models import blogposts
# Create your views here.
def bloglandpage(request):
    querys = blogposts.objects.all()
    num = querys.count()
    if num >= 3:
        posts = reversed(querys.order_by('date')[num-3 : num])
    else:
        posts = reversed(querys)
    fav = blogposts.objects.get(isfav = True)
    #posts = blogposts.objects.all().order_by('-date')[-1]
    arg = {'posts' : posts , 'fav' : fav }
    return render(request , "blog/landingpage.html" , arg)

def allposts(request):
    posts = blogposts.objects.all()
    arg = {"posts" : posts}
    return render(request , "blog/allposts.html" , arg)

def blogdetail(reques , postid):
    post = blogposts.objects.get(id = postid)
    arg = {'post' : post}
    return render(reques , 'blog/postdetail.html' , arg)