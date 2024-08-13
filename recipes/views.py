from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    # return HTTP response
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    # return HTTP response
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })

