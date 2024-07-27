from django.urls import path
from recipes.views import home_view, sobre_view, contato_view

urlpatterns = [
    path('', home_view),  # /home/
    path('sobre/', sobre_view),  # /sobre/
    path('contato/', contato_view),  # /contato/
]
