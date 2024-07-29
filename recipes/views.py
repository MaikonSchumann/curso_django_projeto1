from django.shortcuts import render


def home(request):
    # return HTTP response
    return render(request, 'recipes/home.html', context={
        'name': 'Maikon Schumann',
    })
