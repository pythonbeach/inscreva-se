from django.conf.urls import url
from python_beach_boleto.core import views


urlpatterns = [
    url(r'^$', views.index, name='index')
]
