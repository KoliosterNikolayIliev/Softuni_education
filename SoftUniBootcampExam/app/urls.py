from django.urls import path

from app.views import PostCandidateView, DetailsEditDeleteCandidateView, PostJobView, DeleteJobView, GetRecruiterView, \
    GetInterviewsView

urlpatterns = [

    path('candidates/', PostCandidateView.as_view(), name="post-candidate"),
    path('candidates/<int:pk>/', DetailsEditDeleteCandidateView.as_view(), name="candidate-get-put-delete"),
    path('jobs/', PostJobView.as_view(), name="post-jobs"),
    path('jobs/<int:pk>/', DeleteJobView.as_view(), name="delete-job"),
    path('recruiters/', GetRecruiterView.as_view(), name="get-recruiters"),
    path('interviews/', GetInterviewsView.as_view(), name="get-interviews"),

]
