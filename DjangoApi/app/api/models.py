from django.db import models

# Create your models here.

class MovieCategories(models.Model):
    name = models.CharField(max_length=250)

class Actor(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    age = models.IntegerField(1)

class Director(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    age = models.IntegerField(1)

class Soundtrack(models.Model):
    name = models.CharField(max_length=250)
    release_date = models.DateField()

class Movie(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    ranking = models.IntegerField(1)
    category = models.ForeignKey(MovieCategories, on_delete=models.PROTECT)
    actors = models.ManyToManyField(Actor)
    directors = models.ManyToManyField(Director)
    soundtracks = models.ManyToManyField(Soundtrack)

    #class Meta:
    #   db_table = 'movie'

