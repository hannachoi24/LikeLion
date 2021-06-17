from django.shortcuts import render, get_list_or_404
from .models import Webstaapp
from django.contrib.auth.models import User

# Create your views here.

def feed(request):
    posts = Webstaapp.object.all()
    return render(request, 'feed.html', {'posts': posts})

def profile(request):
    writer = get_list_or_404(User, pk=writer_id)
    writer_posts = writer.post.all()
    return render(request, 'profile.html', {"writer": writer, "writer_posts": writer_posts})