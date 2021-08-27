from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from app.serialisers import CandidateSerializer, JobSerializer, RecruiterSerializer, InterviewSerializer
from app.models import Candidate, Job, Recruiter, Interview


class PostCandidateView(mixins.CreateModelMixin, GenericAPIView):

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class DetailsEditDeleteCandidateView(mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                     GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class PostJobView(mixins.CreateModelMixin, GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    queryset = Job.objects.all()
    serializer_class = JobSerializer


class DeleteJobView(mixins.DestroyModelMixin, GenericAPIView):
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    queryset = Job.objects.all()
    serializer_class = JobSerializer


class GetRecruiterView(mixins.ListModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer


class GetInterviewsView(mixins.ListModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
