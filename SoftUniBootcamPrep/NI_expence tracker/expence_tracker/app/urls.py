from django.urls import path
from .views import home, expense_create, expense_delete, expense_edit, create_profile, profile_edit, profile_delete,profile

# •	http://localhost:8000/ - home page
# •	http://localhost:8000/create - create expense page
# •	http://localhost:8000/edit/:id - edit expense page
# •	http://localhost:8000/delete/:id - delete expense page
# •	http://localhost:8000/profile - profile page
# •	http://localhost:8000/profile/edit - profile edit page
# •	http://localhost:8000/profile/delete - delete profile page


urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile-edit'),
    path('profile/create/', create_profile, name='profile-create'),
    path('profile/delete/', profile_delete, name='profile-delete'),
    path('create/', expense_create, name='expense-create'),
    path('edit/<int:pk>/', expense_edit, name='expense-edit'),
    path('delete/<int:pk>/', expense_delete, name='expense-delete'),
]
