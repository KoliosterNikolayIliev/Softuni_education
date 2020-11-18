from django.urls import path

from main__app import views

urlpatterns = [
    path('', views.index),

]
