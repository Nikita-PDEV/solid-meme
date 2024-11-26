from django.contrib import admin  
from django.urls import path, include  
from news.views import NewsListView  # Импорт представления для списка новостей  

urlpatterns = [  
    path('', NewsListView.as_view(), name='home'),  # корневой маршрут на список новостей  
    path('admin/', admin.site.urls),  # Маршрут для админ-панели  
    path('accounts/', include('allauth.urls')),  # Маршрут для аутентификации через allauth  
    path('news/', include('news.urls')),  # маршрут для приложения news  
]