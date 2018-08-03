from django.shortcuts import render
from profil.models import Posts


def home(request):
    posts=Posts.objects.all()
    return render(request, 'home.html',{
        'posts':posts,
    })
def content(request, id):
    content = Posts.objects.get(id=id)
    return render(request, 'content.html' ,{
    'content':content,
    })

def about(request):
    return render(request, 'about.html')
