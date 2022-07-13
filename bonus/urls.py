from django.urls import path
from .views import ListCreateAPIView, RetrieveDestroyAPIView

urlpatterns = [
    path("bonus/",ListCreateAPIView.as_view()),
    path("bonus/<str:bonus_id>", RetrieveDestroyAPIView.as_view())
    ]