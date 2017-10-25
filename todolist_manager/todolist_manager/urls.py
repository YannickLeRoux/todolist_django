from django.conf.urls import url,include
from django.contrib import admin
from todolists import views

from accounts import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^signup/$', account_views.SignUpView.as_view(), name='signup'),
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'),
    # url(r'^lists/',include('todolists.urls', namespace='lists')),
    # url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    # url(r'^accounts/', include('django.contrib.auth.urls')),

]
