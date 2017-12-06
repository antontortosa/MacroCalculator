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
	# ex: /reg_user/5/add_food
    url(r'^reg_user/(?P<user_id>[0-9]+)/add_food/$', views.add_food, name='add_food'),
    # ex: /reg_user/5/add_food/4/add_ingredient
    url(r'^reg_user/(?P<user_id>[0-9]+)/add_food/(?P<item_id>[0-9]+)/add_ingredient$', views.add_ingredient, name='add_ingredient'),
    
]		