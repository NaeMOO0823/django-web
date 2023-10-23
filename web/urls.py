from django.contrib import admin
from django.urls import path, include
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('', app.views.Index.as_view()),
]
