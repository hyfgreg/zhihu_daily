from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # url(r'^((?P<action>(themes))/)?$', views.Proxy.as_view(), name='proxy'),
    url(r'^((?P<param>(.*?))/)?$', views.Proxy.as_view(), name='proxy'),
    # url(r'theme/(?P<id>\d*)/',views.Proxy_Id.as_view(),name='proxy_id'),
    url(r'^img$', views.IMG_Proxy.as_view(), name='img_proxy'),
]