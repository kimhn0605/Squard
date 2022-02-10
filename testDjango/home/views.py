from django.shortcuts import render
from numpy import require
from user.models import User
from user.decorators import login_required
from django.http import HttpResponse

def hello(request):
    context = {}
    
    login_session = request.session.get('login_session', '')

    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True

    return render(request, 'home/index.html', context)

def dice(request):
    return render(request, 'home/dice.html')

@login_required
def mypage(request):

    login_session = request.session.get('login_session', '')
    context = { 'login_session': login_session }

    if request.method == 'GET':
        return render(request, 'home/mypage.html', context)
    
    elif request.method == 'POST':
        return render(request, 'home/mypage.html', context)
