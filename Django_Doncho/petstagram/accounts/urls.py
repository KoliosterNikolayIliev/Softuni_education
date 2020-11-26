from django.urls import path

from accounts.views import user_profile, signup_user

urlpatterns = [
    path('profile/<int:pk>/', user_profile, name='user_profile'),
    path('signup/', signup_user, name='signup_user'),
]
