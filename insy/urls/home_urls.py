from django.conf.urls import url
from ..views import home_views

urlpatterns = [
    url(r'^$', home_views.home, name='home'),
]
