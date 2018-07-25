from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^additem$', views.add),
    url(r'^confirm$', views.confirm),
    url(r'^clear$', views.clear)
    ]
