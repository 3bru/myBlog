from django.contrib import admin
from django.urls import path
from profil import views

urlpatterns = [
    path('',views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/',views.about, name='about'),
    path('connect/',views.connect, name='connect'),
]
