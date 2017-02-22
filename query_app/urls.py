from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^query_app/latest\.html$',views.index)
]
