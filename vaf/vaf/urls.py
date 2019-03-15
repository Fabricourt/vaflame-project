from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('', include('pages.urls')),
    path('blog/',  include('blog.urls')),
    path('gallery/',  include('gallery.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile, name='profile' ),
 

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
