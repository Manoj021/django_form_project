from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Formfortest'),
    path('submit/', views.success, name='SuccessPage')
]
