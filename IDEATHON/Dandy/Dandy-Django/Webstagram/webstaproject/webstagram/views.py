from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from account.models import Profile
# Create your views here.

def home(request):
    return render(request,'home.html')


#우선은 로그인되어있는 사람 / 아닌사람 식별해서 보여주게만 만들어놨습니다
def myPage(request):
    cur_user=request.user
    print('cur user: ',cur_user)
    if cur_user.is_authenticated:
        user=User.objects.get(email=request.user.email)
        return render(request,'mypage.html',{'user':user})
    else:
        return redirect('login')


def account(request):
    cur_user=request.user
    print('cur user: ',cur_user)
    if cur_user.is_authenticated:
        account=Profile.objects.get(user=cur_user)
        return render(request,'account.html',{'user_profile':account})
    else:
        return redirect('login')