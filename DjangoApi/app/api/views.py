from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from .serializers import *
#from api.serializers import MovieSerializer, MovieCategoriesSerializer

# Create your views here.
#def index(request):
#    return HttpResponse("Hola Clase")

class MovieViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCategoriesViewSet(viewsets.ModelViewSet):
    queryset = MovieCategories.objects.all()
    serializer_class = MovieCategoriesSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class SoundtrackViewSet(viewsets.ModelViewSet):
    queryset = Soundtrack.objects.all()
    serializer_class = SoundtrackSerializer