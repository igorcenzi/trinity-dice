from django.urls import path
from .views import (
    RetrieveAndDeleteJourneyView,
    AddCharToJourneyView,
    ListJourneyCharactersView,
    StartJourneyView,
    EndJourneyView,
    RemoveCharFromJourneyView
)

urlpatterns = [
    path("<str:journey_id>/start/", StartJourneyView.as_view()),
    path("<str:journey_id>/end/", EndJourneyView.as_view()),
    path("<str:journey_id>/", RetrieveAndDeleteJourneyView.as_view()),
    path(
        "<str:journey_id>/characters/<str:char_id>/add/",
        AddCharToJourneyView.as_view(),
    ),
    path('<str:journey_id>/characters/<str:char_id>/remove/', RemoveCharFromJourneyView.as_view()),
    path("<str:journey_id>/characters/", ListJourneyCharactersView.as_view()),
]
