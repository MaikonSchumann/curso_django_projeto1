from django.shortcuts import render


def home(request):
    # return HTTP response
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Maikon Schumann',
    })


def recipe(request, id):
    # return HTTP response
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Luiz Otávio',
    })
    