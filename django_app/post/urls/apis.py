from django.conf.urls import url

from .. import apis as views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),
    url(r'^(?P<pk>[0-9]+)/comment/add/$', views.PostCommentCreate.as_view(), name='comment-add'),
    url(r'^(?P<pk>[0-9]+)/comment/(?P<comment_id>[0-9]+)/delete/$', views.PostCommentDestroy.as_view(),
        name='comment-delete'),
]
