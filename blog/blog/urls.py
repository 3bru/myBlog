from django.contrib import admin
from django.urls import path
from profil import views

urlpatterns = [
    path('',views.home, name='home'),
    path('admin/', admin.site.urls),
    path('content/<int:id>',views.content, name='content'),
    path('about/',views.about, name='about'),

]
