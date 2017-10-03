from django.conf.urls import url
from . import views

urlpatterns = [
    # r'^$' --> http://127.0.0.1:8000/
    # views.post_list --> view
    #
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(regex=r'^drafts/$', view=views.post_draft_list, name='post_draft_list'),
    url(regex=r'^post/(?P<pk>\d+)/publish/$', view=views.post_publish, name='post_publish'),
    url(regex=r'^post/(?P<pk>\d+)/remove/$', view=views.post_remove, name='post_remove'),
    url(regex=r'^post/(?P<pk>\d+)/comment/$', view=views.add_comment_to_post, name='add_comment_to_post'),
    url(regex=r'^comment/(?P<pk>\d+)/approve/$', view=views.comment_approve, name='comment_approve'),
    url(regex=r'^comment/(?P<pk>\d+)/remove/$', view=views.comment_remove, name='comment_remove'),

]
