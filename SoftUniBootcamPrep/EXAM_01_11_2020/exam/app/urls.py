# •	'/' - home page
# •	'/create' - create recipe page
# •	'/edit/:id' - edit recipe page
# •	'/delete/:id' - delete recipe page
# •	'/details/:id' - recipe details page
from django.urls import path

from app.views import IndexView, DetailsView, CreateRecipeView, EditView, DeleteRecipeView

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('create/', CreateRecipeView.as_view(), name='create'),
    path('edit/<int:pk>/', EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', DeleteRecipeView.as_view(), name='delete'),
    path('details/<int:pk>/', DetailsView.as_view(), name='details'),

]

