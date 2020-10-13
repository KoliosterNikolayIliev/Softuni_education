from django.urls import path

from django102.views import UsersListView, GamesListView, something, methods_demo, raises_exception, create_game, \
    index

urlpatterns = [
    path('', index, name='index'),
    path('2/', UsersListView.as_view()),
    path('games/', GamesListView.as_view()),
    path('something/', something),
    path('methods/', methods_demo),
    path('raises/', raises_exception),
    path('creategame/', create_game),
]
