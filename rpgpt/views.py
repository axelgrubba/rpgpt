from django.shortcuts import render


def intro_page(request):
    return render(request, 'intro_page.html', {})
