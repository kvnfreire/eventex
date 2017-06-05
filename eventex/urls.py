from django.conf.urls import include, url
from django.contrib import admin

from eventex.core.views import home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'', include('eventex.subscriptions.urls', namespace='subscriptions')),
    url(r'^admin/', include(admin.site.urls)),
]
