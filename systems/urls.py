from django.urls import path

from journeys.views import ListCreateJourneyView

from .views import ListCreateSystemView, RetrieveDestroySystemView
from items.views import ListCreateItemsView


urlpatterns = [
    path("", ListCreateSystemView.as_view()),
    path("<int:pk>/", RetrieveDestroySystemView.as_view()),
    path("<int:system_id>/items/", ListCreateItemsView.as_view()),
    path("<int:system_id>/journeys/", ListCreateJourneyView.as_view()),
]
