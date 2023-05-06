import random
from django.db import models
from rpgpt.helper_functions import generate_random_name, imagine_characters


class CharacterClass(models.TextChoices):
    BARBARIAN = 'Barbarian'
    BARD = 'Bard'
    CLERIC = 'Cleric'
    DRUID = 'Druid'
    FIGHTER = 'Fighter'
    MONK = 'Monk'
    PALADIN = 'Paladin'
    RANGER = 'Ranger'
    ROGUE = 'Rogue'
    SORCERER = 'Sorcerer'
    WARLOCK = 'Warlock'
    WIZARD = 'Wizard'


class CharacterRace(models.TextChoices):
    HUMAN = 'Human'
    DWARF = 'Dwarf'
    ELF = 'Elf'
    GNOME = 'Gnome'
    GOBLIN = 'Goblin'
    ORC = 'Orc'


class Character(models.Model):
    name: str = models.CharField(max_length=100)
    character_class = models.CharField(max_length=20, choices=CharacterClass.choices)
    race: str = models.CharField(max_length=100)
    hp: int = models.IntegerField(default=100)

    def create_random_character(self) -> None:
        """
        Creates a Character object with random name, class, race and 100 HP.
        """
        Character.objects.create(
            name=generate_random_name(),
            character_class=random.choice(CharacterClass.choices),
            race=random.choice(CharacterRace.choices),
            hp=random.choice(range(20))
        )

    def imagine_character(self) -> None:
        ch = imagine_characters(1, params=["race", "name", "class", "hp"])
        Character.objects.create(
            name=ch[0]['name'],
            character_class=ch[0]['class'],
            race=ch[0]['race'],
            hp=ch[0]['hp'])

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
