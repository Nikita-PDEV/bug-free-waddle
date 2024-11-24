from django.urls import path  
from .views import NewsListView, NewsCreate, ArticleCreate, NewsUpdate, NewsDelete  

urlpatterns = [  
    path('news/', NewsListView.as_view(), name='news_list'),  
    path('news/create/', NewsCreate.as_view(), name='news_create'),  
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),  
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),  
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),  
    path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='article_edit'),  
    path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='article_delete'),  
    path('accounts/', include('allauth.urls')),
    path('become_author/', become_author, name='become_author'),  
    path('subscribe/<int:category_id>/', subscribe_to_category, name='subscribe_to_category'), 
]