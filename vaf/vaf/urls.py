from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from bookings.views import booking
from testaments.views import testament



urlpatterns = [
    path('', include('pages.urls')),
    path('blog/',  include('blog.urls')),
    path('gallery/',  include('gallery.urls')),
    path('accounts/', include('accounts.urls')),
    #path('contact/', include('contact.urls')),
    #path('bookings/', include('bookings.urls')),
    path('partners/', include('partners.urls')),
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile, name='profile' ),
    path('booking/', booking, name='booking'),
    path('testament/', testament, name='testament'),
   

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
