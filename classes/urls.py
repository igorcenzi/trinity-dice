from django.urls import path

from . import views

urlpatterns = [
    path(
        "system/<str:system_id>/classes/",
        views.ListClassView.as_view(),
    ),
    path("classes/<str:class_id>/", views.GetDeleteClassView.as_view()),
]
