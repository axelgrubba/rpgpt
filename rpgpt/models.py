import random
from django.db import models
from rpgpt.helper_functions import generate_random_name, imagine_characters
import openai

openai.api_key = open("./rpgpt/openai_api_key.txt", "r").read().strip()

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
    img_icon_url: str = models.CharField(max_length=400, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpA_2RZ3HMN0pbKHXoNd4UpnBoxkSccoUkUg&usqp=CAU")

    def create_random_character() -> None:
        """
        Creates a Character object with random name, class, race and 100 HP.
        """
        chr = Character.objects.create(
            name=generate_random_name(),
            character_class=random.choice(CharacterClass.choices)[0],
            race=random.choice(CharacterRace.choices)[0],
            hp=random.choice(range(20)),
            img_icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpA_2RZ3HMN0pbKHXoNd4UpnBoxkSccoUkUg&usqp=CAU")
        return chr

    def imagine_character(description) -> None:
        ch = imagine_characters(1, params=["race", "name", "class", "hp"], tags=description.split(' '))
        img_url = openai.Image.create(prompt=description + "DND player icon" + ", ".join(ch[0].values()), n=1, model="image-alpha-001", size="256x256", response_format="url").data[0].url
        chr = Character.objects.create(
            name=ch[0]['name'],
            character_class=ch[0]['class'],
            race=ch[0]['race'],
            hp=ch[0]['hp'],
            img_icon_url=img_url)
        
        return chr

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
