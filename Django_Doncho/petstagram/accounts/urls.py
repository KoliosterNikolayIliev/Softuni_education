from django.contrib.auth.views import LoginView
from django.urls import path, include

from accounts.views import user_profile, signup_user

urlpatterns = [
    # path('signin/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', user_profile, name='user_profile'),
    path('profile/', user_profile, name='current_user_profile'),
    path('signup/', signup_user, name='signup_user'),
]
