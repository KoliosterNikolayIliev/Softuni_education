from django.contrib.auth.models import User
from django.db import models

from accounts.models import UserProfile


class Pet(models.Model):
    PIC = 'pic'
    MOD = 'mod'

    PET_TYPES = (
        (PIC, 'pic'),
        (MOD, 'mod'),

    )

    type = models.CharField(max_length=7, choices=PET_TYPES, default=None)
    name = models.CharField(max_length=6, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='pets')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}; {self.name}; {self.age}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
