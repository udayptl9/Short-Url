from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('srturl/<id>/', views.showurl, name="showurl")
]
