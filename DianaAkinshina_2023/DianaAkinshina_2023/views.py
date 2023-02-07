from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def reversed(request):
    user_text = request.GET['Feedback']
    reversed_text = user_text[::-1]
    return render(request, 'reversed.html', {'reversed': reversed_text})