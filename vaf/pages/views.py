from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def partners(request):
    return render(request, 'pages/partners.html')

def team(request):
    return render(request, 'pages/team.html')

def testimonials(request):
    return render(request, 'pages/testimonials.html')





