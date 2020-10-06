from django.urls import path

from common.views import landing_page, original

urlpatterns = [
    path('original/', original),
    path('', landing_page),
]
