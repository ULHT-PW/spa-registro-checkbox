from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .forms import UserForm

# Create your views here.

def home(request):
    
    return render(request, 'spa/index.html', {'users': User.objects.all()})


def user(request, id):
    
    u = User.objects.get(id = id)
    if request.POST['name'] == 'present':
        if request.POST['checked'] == 'true':
            u.present = True
        else:
            u.present = False
    elif request.POST['name'] == 'online':
        if request.POST['checked'] == 'true':
            u.online = True
        else:
            u.online = False
    u.save()

    return HttpResponse('ok') # empty response
