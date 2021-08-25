"""
    • http://localhost:8000/ - home page
    • http://localhost:8000/create - create expense page
    • http://localhost:8000/edit/:id - edit expense page
    • http://localhost:8000/delete/:id - delete expense page
    • http://localhost:8000/profile - profile page
    • http://localhost:8000/profile/edit - profile edit page
    • http://localhost:8000/profile/delete - delete profile page
"""
from django.urls import path

from app.views import home, CreateExpenseView, EditExpenseView, DeleteExpenseView, profile, profile_edit, profile_delete

urlpatterns = [

    path('', home, name='home page'),
    path('create/', CreateExpenseView.as_view(), name='create expense page'),
    path('edit/<int:pk>/', EditExpenseView.as_view(), name='edit expense page'),
    path('delete/<int:pk>/', DeleteExpenseView.as_view(), name='delete expense page'),
    path('profile/', profile, name='profile page'),
    path('profile/edit/', profile_edit, name='profile edit page'),
    path('profile/delete/', profile_delete, name='delete profile page'),

]
