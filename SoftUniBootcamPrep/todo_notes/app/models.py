from django.db import models

"""
    • Profile
        ◦ first_name - Character field with max length of 20 characters
        ◦ last_name - Character field with max length of 20 characters
        ◦ age - Integer field
        ◦ image_url - URL field
    • Note
        ◦ title - Character field with max length of 30 characters
        ◦ image_url - URL field
        ◦ content - Text field
"""


class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return f"{self.first_name}'s profile"


class Note(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    content = models.TextField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, default=Profile)

    def __str__(self):
        return f'{self.title} note'
