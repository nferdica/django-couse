from django.urls import path
from sisamhil.views import home
    
urlpatterns = [
    path('', home),
]