from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import GenreAPIView, ActorGenericAPIView, CinemaHallViewSet, \
    MovieViewSet

router = DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("genres/", GenreAPIView.as_view(), name="genre-list"),
    path("actors/", ActorGenericAPIView.as_view(), name="actor-list"),
    path("", include(router.urls)),
    path("", include(router.urls))
]

app_name = "cinema"
