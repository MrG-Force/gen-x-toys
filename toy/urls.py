from django.urls import path

from . import views

app_name = 'toy'

urlpatterns = [
    # ex: /toy/8/
    path('<int:pk>/', views.detail, name='detail'),
]
