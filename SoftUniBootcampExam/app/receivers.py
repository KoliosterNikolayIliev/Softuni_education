from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import Recruiter, Candidate, Job, Interview


@receiver(post_save, sender=Candidate)
def create_recruiter(sender, instance, created, **kwargs):
    if created:
        Recruiter.objects.create(candidate=instance)


@receiver(post_save, sender=Candidate)
def save_recruiter(sender, instance, **kwargs):
    instance.recruiter.save()


@receiver(post_save, sender=Job)
def create_and_save_interview(sender, instance, created, **kwargs):
    if created:
        Interview.objects.create(job=instance).save()
