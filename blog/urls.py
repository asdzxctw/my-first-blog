from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^listall/$', views.listall),
    url(r'^post_answer/$', views.post_answer),
    url(r'^allcsv/$', views.allcsv),
]