"""yolowa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from yolowaapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main, name="home"),
    path('account/', include('account.urls')),
    path('health/',views.health,name="health"),
    path('list/',views.list, name="list"),
    path('list/<str:id>',views.sub, name="sub"),
    path('new/', views.new, name="new"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('americas/',views.americas,name='americas'),
    path('asia/',views.asia,name='asia'),
    path('southEastAsia/',views.southEastAsia,name='southEastAsia'),
    path('southPacific/',views.southPacific,name='southPacific'),
    path('europe/',views.europe,name='europe'),
    path('travel/',views.travel,name='travel'),
    path('golf/',views.golf,name='golf'),
    path('culture/',views.culture,name='culture'),
    path('explanation/', views.explanation, name="explanation"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)