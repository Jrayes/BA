from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^Index/', views.index, name='index'),
    url(r'^ProcessUrls/', views.get_urls),
    url(r'^validate/', views.Success),
]
