from django.conf.urls import url

from . import views


app_name = 'app_1'

urlpatterns = [
    # ex: /profile/
    url(r'^profile/$', views.index, name='index'),
    # ex: /profile/5/
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    # ex: /profile/5/history/
    url(r'^profile/(?P<user_id>[0-9]+)/history/$', views.history, name='history'),
]		