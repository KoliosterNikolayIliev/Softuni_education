from django.urls import path

from formslab.views import formslab

urlpatterns = [
    path('', formslab, name='formslab')
]
