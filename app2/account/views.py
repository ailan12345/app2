from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from account.models import User
from app2.settings import DEBUG


#from app2.settings import DATABASES
def account(request):
    if DEBUG:
        print('LOCAL')
        return render(request,'account/account.html',{'users':User.objects.all()})
    print('HEROKU')
    return render(request,'account/account.html',{'users':User.objects.using('user').all()})




def login(request):
    user = authenticate(username='admin', password='admin')
    if user:
        auth_login(request, user)
    else:
        print('NoAdmin')
    return redirect('account:account')


