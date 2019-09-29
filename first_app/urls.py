from django.urls import path, re_path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help, name="help"),
    path('users', views.users, name="users"),
    path('forms', views.forms, name="forms"),
    path('sign-up', views.newUser, name = 'signup'),
    path('relative', views.relative, name = 'relative'),
    path('other', views.other, name = 'other'),
    re_path(r'^.*/$', views.noPage, name="error")
]
