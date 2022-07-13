from django.urls import path

from . import views

urlpatterns = [
    path("classes/", views.ListCreateClassView.as_view()),
    path("classes/<str:class_id>/", views.GetDeleteClassView.as_view()),
]
