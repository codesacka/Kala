from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
        # path('', views.list, name='accountclass_list'),
]