from django.urls import path
from .views import BonusView, BonusDetailView

urlpatterns = [
    path("", BonusView.as_view()),
    path("<str:pk>/", BonusDetailView.as_view()),
]
