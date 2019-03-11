from django.urls import path
from django.shortcuts import redirect

from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('contact', views.contact, name='contact'),
    path('partners', views.partners, name='partners'),
    
]



