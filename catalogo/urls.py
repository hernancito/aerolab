from django.conf.urls import url

from views import catalogo

urlpatterns = [
    url(r'^$', catalogo, name='catalogo'),
]
