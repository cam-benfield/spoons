from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^task_list', views.task_list, name='tasks'),
    url(r'^user_list', views.user_list, name='users'),

]
