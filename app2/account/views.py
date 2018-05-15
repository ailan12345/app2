from django.shortcuts import render

from account.models import User
from app2.settings import DEBUG


#from app2.settings import DATABASES
def account(request):
    if DEBUG:
        print('LOCAL')
        return render(request,'account/account.html',{'users':User.objects.all()})
    print('HEROKU')
    return render(request,'account/account.html',{'users':User.objects.using('user').all()})
