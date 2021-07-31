
from myshop.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include("shop.urls")),
    path('blog/',include("blog.urls"))              
]  + static(settings.MEDIA_URL, documents_roots= settings.MEDIA_ROOT)

