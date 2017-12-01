from django.conf.urls import url

from . import views


app_name = 'app_1'

urlpatterns = [
    # ex: /reg_user/
    url(r'^reg_user/$', views.index, name='index'),
    # ex: /reg_user/5/
    url(r'^reg_user/(?P<user_id>[0-9]+)/$', views.reg_user, name='reg_user'),
    # ex: /reg_user/5/history/
    url(r'^reg_user/(?P<user_id>[0-9]+)/history/$', views.history, name='history'),
]		