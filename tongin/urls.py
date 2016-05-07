from django.conf.urls import url,patterns,include
from django.contrib import admin
from dosirak.views import index
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dosirak/', include('dosirak.urls')),

]
