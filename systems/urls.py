from django.urls import path

from .views import ListCreateSystemView, RetrieveDestroySystemView


urlpatterns = [
    path("", ListCreateSystemView.as_view()),
    path("<str:pk>/", RetrieveDestroySystemView.as_view()),
]
