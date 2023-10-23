from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('tag', views.Tag.as_view(), name='tag')
]