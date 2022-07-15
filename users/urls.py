from django.urls import path
from . import views


urlpatterns = [
    path("", views.ListCreateUserView.as_view()),
    path("<str:user_id>/", views.ListUserDetailsView.as_view()),
]
