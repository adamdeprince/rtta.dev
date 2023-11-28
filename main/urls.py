from django.urls import path, register_converter

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('install', views.install, name='install'),
    path('overview', views.overview, name='overview')
]
