from django.urls import path
from . import views

app_name = 'idealab'
urlpatterns = [
	path('', views.index, name='index'),
]
