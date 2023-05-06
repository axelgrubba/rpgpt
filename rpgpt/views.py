from django.shortcuts import render


def intro_page(request):
    return render(request, 'intro.html', {})


def character_creation(request):
    return render(request, 'character_creation.html', {})


def story_creation(request):
    return render(request, 'story_creation.html', {})


def game_intro(request):
    return render(request, 'game_intro.html', {})


def game(request):
    return render(request, 'game.html', {})
