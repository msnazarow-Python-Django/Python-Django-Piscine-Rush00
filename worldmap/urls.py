from . import views
from django.urls import path, include
# app_name = 'options'
urlpatterns = [
	path('', views.WorldmapView.as_view(), name='worldmap'),
]
