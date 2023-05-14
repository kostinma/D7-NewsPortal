from django.urls import path

from .views import (
PostList,
   PostDetail,
   SearchPostList,
   PostCreate,
   PostDelete,
   PostUpdate,
)

urlpatterns = [
   path('news/', PostList.as_view(), name = 'post_list'),
   path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/search/', SearchPostList.as_view(), name='news_search'), # GET queries are possible

   path('news/create/',          PostCreate.as_view(), name='news_create'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('news/<int:pk>/edit/',   PostUpdate.as_view(), name='news_edit'),

   path('article/create/',          PostCreate.as_view(), name='article_create'),
   path('article/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),
   path('article/<int:pk>/edit/',   PostUpdate.as_view(), name='article_edit'),
]
