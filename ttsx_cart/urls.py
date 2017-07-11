from django.conf.urls import url

from ttsx_cart import views


urlpatterns = [
    url(r'^cart/$', views.cart)
]