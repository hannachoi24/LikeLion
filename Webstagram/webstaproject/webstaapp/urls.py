from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

URLPattern = [
    path('profile/<int:writer_id>', profile, name="profile")
]