from django.db import models


# class Skills(models.Model):
#     name = models.CharField(max_length=240, db_index=True)


class Candidate(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    bio = models.TextField()
    birth_date = models.DateField()
    skills = models.JSONField()

    def __str__(self):
        return f'{self.id};{self.first_name}'


class Recruiter(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, blank=False)
    experience_level = models.IntegerField(default=1)


class Job(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    salary = models.FloatField()
    skills = models.JSONField()


class Interview(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=False)
