from django.urls import path

from .views import ListCreateCharView


urlpatterns = [
    path("", ListCreateCharView.as_view()),
]
