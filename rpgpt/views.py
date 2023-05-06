from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import rpgpt.models
from rpgpt.models import Character
import openai
from django.http import JsonResponse

USE_AI_CHARACTERS = False


def intro_page(request):
    return render(request, "intro.html", {})


@csrf_exempt
def character_creation(request):
    print(request)
    random_characters = dict()
    for i in range(1, 5, 1):
        char = Character.create_random_character()
        random_characters[f"random{i}"] = {
            "name": char.name,
            "race": char.race,
            "class": char.character_class,
        }

    if request.method == "POST":
        character_description = request.POST.get("comment")
        if USE_AI_CHARACTERS:
            character = rpgpt.models.Character.imagine_character(character_description)
        else:
            character = rpgpt.models.Character.create_random_character()

        return render(
            request,
            "character_creation.html",
            {
                "name": character.name,
                "race": character.race,
                "class": character.character_class,
                "hp": character.hp,
                "icon": character.img_icon_url,
                **random_characters,
            },
        )

    return render(
        request,
        "character_creation.html",
        {
            "name": "Ricky",
            "race": "Human",
            "class": "Pickle",
            "icon": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpA_2RZ3HMN0pbKHXoNd4UpnBoxkSccoUkUg&usqp=CAU",
            **random_characters,
        },
    )


def story_creation(request):
    return render(request, "story_creation.html", {})


def game_intro(request):
    character = Character.objects.latest("id")
    return render(
        request,
        "game_intro.html",
        {
            "name": character.name,
            "race": character.race,
            "class": character.character_class,
        },
    )


# def game(request):
#     return render(request, "game.html", {})


def chat(request):
    chats = rpgpt.models.Chat.objects.all()
    return render(
        request,
        "chat.html",
        {
            "chats": chats,
        },
    )


@csrf_exempt
def Ajax(request):
    if (
        request.headers.get("X-Requested-With") == "XMLHttpRequest"
    ):  # Check if request is Ajax
        text = request.POST.get("text")
        print(text)

        openai.api_key = "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"  # Here you have to add your api key.
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{text}"}]
        )

        response = res.choices[0].message["content"]
        print(response)

        chat = rpgpt.models.Chat.objects.create(text=text, gpt=response)

        return JsonResponse(
            {
                "data": response,
            }
        )
    return JsonResponse({})
