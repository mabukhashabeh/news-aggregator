from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListNews.as_view(), name="home"),
    path('scrape/', views.scrape, name="scrape"),

]
