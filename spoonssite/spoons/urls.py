from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^task_list', views.task_list, name='tasks'),
    url(r'^user_list', views.user_list, name='users'),
    url(r'^task/(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    url(r'^user/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    url(r'^task/new/$', views.task_new, name='task_new'),
    url(r'^user/new/$', views.user_new, name='user_new'),
    url(r'^user_query', views.user_query, name = 'user_query'),
    url(r'^task_query', views.task_query, name = 'task_query'),
]
