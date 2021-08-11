"""webstaproject URL Configuration

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
from django.urls import path
from webstagram import views as websta
from account import views as acc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',websta.home,name='home'),
    path('signIn/',acc.login_user,name='login'),
    path('logout/',acc.logout_user,name='logout'),
    path('signUp/',acc.signUp,name='signUp'),
    path('mypage/',websta.myPage,name='mypage'),
    path('account/',websta.account,name='account'),
    path('findEmail/',acc.find_email,name='findEmail'),
    path('findPwd/',acc.find_pwd,name='findPwd'),
    path('changePwd/<str:usermsg>',acc.changePwd,name='changePwd'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
