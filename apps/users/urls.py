from django.conf.urls import url
from views import register, login, new, users


urlpatterns = [
    url(r'^$', register),
    url(r'^login', login),
    url(r'^new', new),
    url(r'^users', users),

]