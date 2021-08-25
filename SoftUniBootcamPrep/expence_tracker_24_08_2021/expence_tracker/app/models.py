from django.db import models

"""
    • Profile
        ◦ first_name - Character field with max length of 15 characters
        ◦ last_name - Character field with max length of 15 characters
        ◦ budget – Integer field
    • Expense
        ◦ title - Character field with max length of 50 characters
        ◦ image_url - URL field
        ◦ description - Text field
        ◦ price - Float field
"""


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField()

    def __str__(self):
        return f'{self.first_name}\'s profile'


class Expense(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, default=Profile)

    def __str__(self):
        return f'{self.title} expense'
