from django.urls import path
from .views import BonusView, BonusDetailView

urlpatterns = [
    path("bonus/", BonusView.as_view()),
    path("bonus/<str:pk>/", BonusDetailView.as_view()),
]
