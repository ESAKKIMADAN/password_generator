from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.generator, name='generator'),
]
