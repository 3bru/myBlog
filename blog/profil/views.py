from django.shortcuts import render
from profil.models import Posts


def home(request):
    text=Posts.objects.all()
    return render(request, 'home.html',{
        'title': 'ilkyazı',
        'posts': 'icerik',
    })

def about(request):
    return render(request, 'about.html')

def connect(request):
    return render(request, 'connect.html')
