from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import rpgpt.models
from django.http import HttpResponseRedirect
from django.urls import reverse

def intro_page(request):
    return render(request, 'intro.html', {})

@csrf_exempt
def character_creation(request):
    print(request)
    if request.method == 'POST':
        character_description = request.POST.get('comment')
        character = rpgpt.models.Character.imagine_character(character_description)
    
        return render(request, 'character_creation.html',
                      {"name": character.name,
                       "race": character.race,
                       "class": character.character_class,
                       "hp": character.hp,
                       "icon": character.img_icon_url })

    return render(request, 'character_creation.html', {"name": "Ricky", "race": "Human", "class": "Pickle",
                        "icon": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpA_2RZ3HMN0pbKHXoNd4UpnBoxkSccoUkUg&usqp=CAU" })


def story_creation(request):
    return render(request, 'story_creation.html', {})


def game_intro(request):
    return render(request, 'game_intro.html', {})


def game(request):
    return render(request, 'game.html', {})
