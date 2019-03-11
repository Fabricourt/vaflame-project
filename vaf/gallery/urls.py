from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<int:gallery_id>', views.gallery, name='gallery-id'),
    
    
]



