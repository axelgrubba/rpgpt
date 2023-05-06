

"""
URL configuration for rpgpt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import rpgpt.views as views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.intro_page, name='intro_page'),
    path('character-creation', views.character_creation, name="character_creation"),
    path('story-creation', views.story_creation, name="story_creation"),
    path('game-intro', views.game_intro, name="game_intro"),
    path('game', views.game, name="game"),
]
