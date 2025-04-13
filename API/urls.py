from django.contrib import admin
from django.urls import path
from API import views

app_name = 'API'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('search/', views.word_search, name="search")
]