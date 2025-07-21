from django.contrib import admin
from django.urls import path
from API import views

app_name = 'API'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name="home"),
    path('search/', views.SearchView.as_view(), name="search")
]