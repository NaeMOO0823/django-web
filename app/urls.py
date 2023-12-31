from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('account', views.Account.as_view(), name='account'),
    path('test', views.Test.as_view(), name='test'),
    path('tetris', views.Tetris.as_view(), name='tetris')
]