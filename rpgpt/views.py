from django.shortcuts import render


def intro_page(request):
    return render(request, 'default_page.html', {})


def character_creation(request):
    return render(request, 'default_page.html', {})


def story_creation(request):
    return render(request, 'default_page.html', {})


def game_intro(request):
    return render(request, 'default_page.html', {})


def game(request):
    return render(request, 'default_page.html', {})
