from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('run', 'Run'),
        ('cycle', 'Cycle'),
        ('swim', 'Swim'),
        ('walk', 'Walk'),
    ]
    user_id = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=ACTIVITY_TYPES)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    distance = models.FloatField(help_text='Distance in km')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text='Duration in minutes')

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    user_id = models.CharField(max_length=100)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user_id}: {self.points} pts"
