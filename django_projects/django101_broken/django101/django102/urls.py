from django.urls import path

from django102.views import index, UsersListView, GamesListView, something, methods_demo, raises_exception

urlpatterns = [
    path('', index),
    path('2/', UsersListView.as_view()),
    path('games/', GamesListView.as_view()),
    path('something/', something),
    path('methods/', methods_demo),
    path('raises/', raises_exception),
]
