from django.urls import path

from app.views import AddNoteView, EditNoteView, DeleteNoteView, DetailsView, home, profile

"""
    • http://localhost:8000/ - home page
    • http://localhost:8000/add - add note page
    • http://localhost:8000/edit/:id - edit note page
    • http://localhost:8000/delete/:id - delete note page
    • http://localhost:8000/details/:id - note details page
    • http://localhost:8000/profile - profile page
"""

urlpatterns = [

    path('', home, name='home page'),
    path('add/', AddNoteView.as_view(), name='add note page'),
    path('edit/<int:pk>/', EditNoteView.as_view(), name='edit note page'),
    path('delete/<int:pk>/', DeleteNoteView.as_view(), name='delete note page'),
    path('details/<int:pk>/', DetailsView.as_view(), name='note details page'),
    path('profile/', profile, name='profile page'),

]
