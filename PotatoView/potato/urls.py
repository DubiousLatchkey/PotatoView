from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^potatoes/$', views.PotatoList.as_view()),
    url(r'^potatoes/(?P<id>[0-9]+)/$', views.PotatoDetail.as_view()),
]

