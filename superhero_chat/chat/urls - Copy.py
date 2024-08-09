from django.urls import path
from . import views

urlpatterns = [
  path('', views.select_hero, name='select_hero'),
  path('chat/<int:hero_id>/', views.chat, name='chat'),
  path('generate_response/', views.generate_response, name='generate_response'),
  path('exit_chat/', views.exit_chat, name='exit_chat'),
  path('change_hero/', views.change_hero, name='change_hero'),
]