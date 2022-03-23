
from django.urls import re_path
from UserApp import views


urlpatterns=[

    re_path(r'^role/$', views.roleApi),
    re_path(r'^role/([0-9]+)$', views.roleApi)

]