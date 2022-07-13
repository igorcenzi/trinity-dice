from django.urls import path

from . import views

urlpatterns = [
    path("classes/", views.ListCreateClassView.as_view()),
    path("classes/<int:num>/", views.GetDeleteClassView.as_view()),
]
