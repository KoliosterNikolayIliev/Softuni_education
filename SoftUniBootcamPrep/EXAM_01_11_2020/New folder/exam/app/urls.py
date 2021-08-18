# •	'/' - home page
# •	'/create' - create recipe page
# •	'/edit/:id' - edit recipe page
# •	'/delete/:id' - delete recipe page
# •	'/details/:id' - recipe details page
from django.urls import path

from app.views import index, create, edit, details, delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('details/<int:pk>/', details, name='details'),
]
