from django.conf.urls import url

from index import views

urlpatterns = [
    url(r'^$',views.index_view,name='index'),
]