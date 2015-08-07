from django.conf.urls import url
from python_beach_boleto.core import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recupera-boleto/$', views.recovery_by_email, name='recovery'),
    # url(r'^payment/(?P<id_enroll>\d+)$', views.payment, name='payment')
    # url(r'^payment/$', views.payment, name='payment')
]
