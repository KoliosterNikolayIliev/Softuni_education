from django.urls import path

from pets import views


urlpatterns = [
    path('', views.pet_list, name='pet list'),
    path('details/<int:pk>/', views.pet_details, mane='pet_details'),#<int:pk> - take the pet object using pk (id)
    path('like/<int:pk>/', views.like_pet, name='like pet'),
    #copied from Doncho's:
    path('delete/<int:pk>/', delete_pet, name='delete pet'),
    path('create/', create_pet, name='create pet'),
]