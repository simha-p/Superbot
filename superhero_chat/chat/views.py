

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Hero
import google.generativeai as genai
import os

# Configure the Google AI API
genai.configure(api_key="AIzaSyBPp1e1otizv7GeIjYM_IQzVgrU3wWwKS8")

def select_hero(request):
  heroes = Hero.objects.all()
  return render(request, 'select_hero.html', {'heroes': heroes})

def chat(request, hero_id):
  hero = Hero.objects.get(id=hero_id)
  user_icon = request.user.first_name if request.user.is_authenticated else 'Guest'
  return render(request, 'chat.html', {'hero': hero, 'user_icon':user_icon})

def generate_response(request):
  if request.method == 'POST':
      user_message = request.POST.get('message')
      hero_id = request.POST.get('hero_id')
      hero = Hero.objects.get(id=hero_id)
      
      # Use Google AI API to generate response
      model = genai.GenerativeModel('gemini-pro')
      prompt = f"As {hero.name}, respond to: {user_message}"
      response = model.generate_content(prompt)
      
      return JsonResponse({'response': response.text})

def exit_chat(request):
  return redirect('select_hero')

def change_hero(request):
  return redirect('select_hero')