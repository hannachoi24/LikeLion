"""blog URL Configuration

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
from blogapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('<str:id>', detail, name="detail"),
]

""" <str:id>: <자료형:(views.py)에 정의한 매개변수이름> 데이터 베이스의 데이터(id)에 따라 페이지가 다르게 보이기도하고 views.py의 매개변수로 들어가기도함 """
""" 즉, url로 path convert를 적어주면 id값을 통해 페이지가 다르게 보여질 수 있고 views.py에 있는 매개변수로 옮겨줄 수도 있다 """