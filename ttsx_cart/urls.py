from django.conf.urls import url

from ttsx_cart import views


urlpatterns = [
    url(r'^cart/$', views.cart),
    url(r'^add/$', views.add),
    url(r'^count/$', views.count),
]