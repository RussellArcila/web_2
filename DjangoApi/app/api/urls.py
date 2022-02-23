from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'moviecategories', views.MovieCategoriesViewSet)
router.register(r'actors', views.ActorViewSet)
router.register(r'directors', views.DirectorViewSet)
router.register(r'soundtracks', views.SoundtrackViewSet)

urlpatterns = [
    #path('', views.index, name='index'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace= 'rest_framework'))
]