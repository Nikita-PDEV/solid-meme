# news/urls.py  

from django.urls import path  
from .views import NewsListView, PostList, PostDetail, PostCreate, PostEdit, PostDelete  

urlpatterns = [  
    path('', NewsListView.as_view(), name='news_list'), 
    path('news/<int:post_id>/', PostDetail.as_view(), name='post_detail'),  
    path('news/create/', PostCreate.as_view(), name='post_create'),  
    path('news/<int:post_id>/edit/', PostEdit.as_view(), name='post_edit'),  
    path('news/<int:post_id>/delete/', PostDelete.as_view(), name='post_delete'),  
]