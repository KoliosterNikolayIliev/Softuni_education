from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Pet(models.Model):
    DOG = 'Dog'
    CAT = 'Cat'
    PARROT = 'Parrot'
    PET_TYPES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        ('animal', 'animal'),

    )
    type = models.CharField(max_length=6, default='animal', choices=PET_TYPES, blank=False)
    name = models.CharField(max_length=6)
    # age = models.IntegerField(validators=[MinValueValidator(0)], blank=False)
    age = models.PositiveIntegerField(blank=False)
    description = models.TextField(default=None)
    image_url = models.URLField(default=None, blank=False)

    def __str__(self):
        return f'ID - {self.id};  NAME - {self.name}; AGE - {self.age}'


class Like(models.Model):
    default = 'like'
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    like = models.CharField(max_length=4, default=default, blank=None)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
