from django.conf.urls import url,include
from django.contrib import admin
from todolists import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePageView.as_view(), name='home'),
    # url(r'^lists/',include('todolists.urls', namespace='lists')),
    # url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    # url(r'^accounts/', include('django.contrib.auth.urls')),

]
