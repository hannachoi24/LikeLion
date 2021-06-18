from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<int:writer_id>', profile, name="profile"),
]