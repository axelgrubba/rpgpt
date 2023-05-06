from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import rpgpt.models

USE_AI_CHARACTERS = False
from rpgpt.models import Character

def intro_page(request):
    return render(request, 'intro.html', {})

@csrf_exempt
def character_creation(request):
    print(request)
    random_characters = dict()
    for i in range(1, 5, 1):
        char = Character.create_random_character()
        random_characters[f"random{i}"] = {"name": char.name, "race": char.race, "class": char.character_class}

    if request.method == 'POST':
        character_description = request.POST.get('comment')
        if USE_AI_CHARACTERS:
            character = rpgpt.models.Character.imagine_character(character_description)
        else:
            character = rpgpt.models.Character.create_random_character()

        return render(request, 'character_creation.html',
                      {"name": character.name,
                       "race": character.race,
                       "class": character.character_class,
                       "hp": character.hp,
                       "icon": character.img_icon_url,
                       **random_characters
                       })

    return render(request, 'character_creation.html', {"name": "Ricky", "race": "Human", "class": "Pickle",
                        "icon": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpA_2RZ3HMN0pbKHXoNd4UpnBoxkSccoUkUg&usqp=CAU",
                                                       **random_characters})


def story_creation(request):
    return render(request, 'story_creation.html', {})


def game_intro(request):
    return render(request, 'game_intro.html', {})


def game(request):
    return render(request, 'game.html', {})
