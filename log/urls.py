# log/urls.py
from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout

# We are adding a URL called /home
urlpatterns = [
    url(r'login/$', views.index, name='index'),
    url(r'Register/$', views.register, name='register'),
    url(r'^sair/$', logout,{'next_page':'index'},name='logout'),
    url(r'home/$', views.home, name='home'),

]
