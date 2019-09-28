from django.urls import path, re_path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help, name="help"),
    path('users', views.users, name="users"),
    path('forms', views.forms, name="forms"),
    re_path(r'^.*/$', views.noPage, name="error")
]
