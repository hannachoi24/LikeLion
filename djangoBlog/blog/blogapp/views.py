from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request,id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    form = BlogForm()
    return render(request, 'new.html',{'form':form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_data = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')    

    """ new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']    
    new_blog.body = request.POST['body']
    new_blog.pub_data = timezone.now()
    new_blog.save() """

    

def edit(request, id): 
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': 'edit_blog'})

""" id역할: 어떤 부분을 수정할지 알아야하기 때문에 """

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']    
    update_blog.body = request.POST['body']
    update_blog.pub_data = timezone.now()
    update_blog.save() 
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')