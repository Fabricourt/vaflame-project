from django.urls import path
from . import views 


urlpatterns = [
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('gallery/<int:pk>', views.GalleryDetailView.as_view(), name='gallery-detail'),
  
]


