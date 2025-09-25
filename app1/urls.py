from django.urls import path
from . import views

urlpatterns = [
    path('', views.app1, name='app1'),
    path('app/app2', views.app2, name='app2'),
]

