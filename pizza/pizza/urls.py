#from django.urls import path, include
from django.conf.urls import url, include
from django.contrib import admin
from authapp import views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),

    url(r'authapp/login/$', auth_views.LoginView.as_view(
    template_name='authapp/login.html'), name='authapp-login'),
    url(r'authapp/logout/$', auth_views.LogoutView.as_view(
    next_page='/'), name='authapp-logout'),
    url(r'authapp/$', views.authapp_home, name='authapp-home'),
    url(r'authapp/sign-up$', views.authapp_sign_up, name='authapp-sign-up'),
    #url(r'^formpage/', views.form_page, name='form-page'),
    #url(r'^(?P<pizza_id>\d+)/$', views.pizza_detail, name='pizza_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
