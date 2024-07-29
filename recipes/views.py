from django.shortcuts import render


def home(request):
    # return HTTP response
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Maikon Schumann',
    })
