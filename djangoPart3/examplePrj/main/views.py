from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs= Blog.objects.all()
    return render(request,"home.html",{"blogs":blogs})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog=Blog()
    new_blog.title=request.POST['title']
    new_blog.body=request.POST['body']
    new_blog.pub_date= timezone.now()
    new_blog.author=request.POST['author'] #바뀔부분
    new_blog.save()
    return redirect('home')

def detail(request, blog_id) :
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {"blog":blog})

def profile(request):
    return render(request, 'profile.html')

