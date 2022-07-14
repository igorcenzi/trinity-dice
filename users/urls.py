from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("", views.ListCreateUserView.as_view()),
    path("<str:user_id>/", views.ListUserDetailsView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
