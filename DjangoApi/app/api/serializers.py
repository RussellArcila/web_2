from .models import *
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'ranking', 'category', 'actors', 'directors', 'soundtracks']
    
    def to_representation(self, instance):
        ret =  super().to_representation(instance)
        return {
            'id': ret['id'],
            'name': ret['name'],
            'description': ret['description'],
            'category_id': ret['category'],
            'actors': ret['actors'],
            'directors': ret['directors'],
            'soundtracks': ret['soundtracks']
        }


class MovieCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCategories
        fields = ['id', 'name']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'surname', 'age']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'surname', 'age']

class SoundtrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soundtrack
        fields = ['id', 'name', 'release_date']