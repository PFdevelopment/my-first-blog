from django.conf.urls import url
from . import views

urlpatterns = [
    # r'^$' --> http://127.0.0.1:8000/
    # views.post_list --> view
    #
    url(r'^$', views.post_list, name='post_list')
]
