from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post,Category


# Create your views here.
def home(request):
    posts=Post.objects.all()[:11]
    #print

    cats=Category.objects.all()
    data = {
        'posts':posts,
        'cats': cats
    }
    return render(request,'Home.html',data)

def post(request,url):
    post=Post.objects.get(url=url)
    return render(request, 'post.html', {'post': post})