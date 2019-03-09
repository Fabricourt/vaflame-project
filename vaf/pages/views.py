from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')


def team(request):
    return render(request, 'pages/team.html')

def partners(request):
    return render(request, 'pages/partners.html')


def testimonials(request):
    return render(request, 'pages/testimonials.html')

def blog(request):
    return render(request, 'pages/blog.html')
