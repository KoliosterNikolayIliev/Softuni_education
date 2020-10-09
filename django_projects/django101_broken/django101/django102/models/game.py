from django.db import models

from django102.models.player import Player


class Game(models.Model):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    DIFFICULTY_LEVELS = (
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Hard')
    )
    name = models.CharField(max_length=30, blank=False, default='')
    level_of_difficulty = models.IntegerField(blank=False,
    choices=DIFFICULTY_LEVELS, default=EASY)
    players = models.ManyToManyField(Player)




