from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='action')
    serializer_class = MovieSerializer    

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='comedy')
    serializer_class = MovieSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='anime')
    serializer_class = MovieSerializer

class ScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='science fiction')
    serializer_class = MovieSerializer