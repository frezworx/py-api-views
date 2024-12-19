from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreAPIView,
    CinemaHallViewSet,
    MovieViewSet,
    ActorList,
    ActorDetail,
)

router = DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("genres/", GenreAPIView.as_view(), name="genre-list"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("", include(router.urls)),
    path("", include(router.urls))
]

app_name = "cinema"
