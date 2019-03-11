from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from.models import Gallery

def gallery(request):
  gallery = Gallery.objects.order_by('-gallery_date').filter(is_published=True)

  paginator = Paginator(gallery, 12)
  page = request.GET.get('page')
  paged_gallery = paginator.get_page(page)

  context = {
    'gallery': paged_gallery
  }

  return render(request, 'gallery/gallery.html', context)


"""def gallery(request, gallery_id):
  gallery = get_object_or_404(Gallery, pk=gallery_id)

  context = {
    'gallery': gallery
  }"""



