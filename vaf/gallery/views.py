from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import  Gallery


def index(request):
    return render(request, 'gallery/index.html')


class GalleryListView(generic.ListView):
    """Generic class-based view for a list of gallery."""
    model = Gallery
    paginate_by = 5
    
   
    
class GalleryDetailView(generic.DetailView):
    """Generic class-based detail view for a gallery_detail."""
    model = Gallery
    
   


