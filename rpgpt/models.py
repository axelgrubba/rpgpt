from django.db import models
from rpgpt.helper_functions import generate_name


class Character(models.Model):
    name: str = models.CharField(max_length=100, default=generate_name())
    character_class: str = models.CharField(max_length=100)
    race: str = models.CharField(max_length=100)
    hp: int = models.IntegerField()


class Story(models.Model):
    """
    A story consists of:
    - A collection of Character objects
    - A collection of StoryState objects
    """
    characters = models.ManyToManyField('Character', related_name='story')
    states = models.ManyToManyField('StoryState', related_name='story')


class StoryState(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    environment_description: str = models.TextField()
    weather: str = models.CharField(max_length=200)
    chosen_actions: str = models.JSONField()  # mapping of characters to string actions
    outcome: str = models.TextField()
