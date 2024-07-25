from django.urls import path
from recipes.views import home_view, sobre_view, contato_view

urlpatterns = [
    path('sobre/', sobre_view),  # /sobre/
    path('', home_view),  # /home/
    path('contato/', contato_view),  # /contato/
]
