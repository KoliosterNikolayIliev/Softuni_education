from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.FloatField()



class Expense(models.Model):
    title = models.CharField(max_length=50)
    link_to_image = models.URLField()
    description = models.TextField()
    price = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
