from django.conf.urls import url
#from django.urls import path, include
from testurlapp import views

urlpatterns = [
    url(r'^user/(\d+)/$', views.home, name='home'),
    #path('user/(\d+)/', views.home, name='home'),
    #site.com/user/12
]
