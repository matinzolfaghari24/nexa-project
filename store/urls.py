from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]