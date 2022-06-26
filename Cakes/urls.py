from django.conf.urls import url
from django.conf.urls.static import static

from django.conf import settings
from . import views

app_name = 'Cakes'

urlpatterns = [
    # /home/
    # url(r'^$', views.home.as_view(), name='home'),

]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)