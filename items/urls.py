from django.urls import path
from .views import (
    ListCreateItemsView,
    RetrieveDestroyItemsView,
    ApplyBonusView,
    RemoveBonusView,
)

urlpatterns = [
    path("", ListCreateItemsView.as_view()),
    path("<str:pk>/", RetrieveDestroyItemsView.as_view()),
    path("<str:pk>/apply/<str:bonus_id>/", ApplyBonusView.as_view()),
    path("<str:pk>/remove/<str:bonus_id>/", RemoveBonusView.as_view()),
]
