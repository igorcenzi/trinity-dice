from django.urls import path
from .views import (
    ListCreateJourneyView,
    RetrieveAndDeleteJourneyView,
    RetrieveAndUpdateAddJourneyCharactersView,
    RetrieveJourneyCharactersView,
    UpdateStartedJourneyView,
    UpdateEndedJourneyView,
)

urlpatterns = [
    path("<str:journey_id>/start/", UpdateStartedJourneyView.as_view()),
    path("<str:journey_id>/end/", UpdateEndedJourneyView.as_view()),
    path("<str:journey_id>/", RetrieveAndDeleteJourneyView.as_view()),
    path(
        "<str:journey_id>/characters/<str:char_id>/add/",
        RetrieveAndUpdateAddJourneyCharactersView.as_view(),
    ),
    # path('<str:journey_id>/characters/<str:char_id>/remove', RetrieveAndUpdateDelJourneyCharactersView.as_view()),
    path("<str:journey_id>/characters/", RetrieveJourneyCharactersView.as_view()),
]
