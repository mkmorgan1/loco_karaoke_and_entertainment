from django.urls import path
from . import views

app_name = 'karaoke'

urlpatterns = [
    path('', views.home, name='home'),
] 