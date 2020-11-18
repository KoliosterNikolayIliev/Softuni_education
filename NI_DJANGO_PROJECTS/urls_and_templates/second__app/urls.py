from django.urls import path

from second__app import views

urlpatterns = [
    path('', views.index)
]
