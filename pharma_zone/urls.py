from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'pharma_zone'

urlpatterns = [
    url(r'^$', views.product_list, name='medical_product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]