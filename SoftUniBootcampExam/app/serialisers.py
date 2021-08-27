from rest_framework import serializers

from app.models import Candidate, Job, Recruiter, Interview


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = (
            'first_name',
            'last_name',
            'email',
            'bio',
            'birth_date',
            'skills'
        )


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'title',
            'description',
            'salary',
            'skills',
        )


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'
