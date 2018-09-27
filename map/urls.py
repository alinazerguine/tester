from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usa/', views.usa, name='usa'),
    path('nebraska/', views.nebraska, name='nebraska')
    ]