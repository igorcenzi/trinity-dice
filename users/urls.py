from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('users/', views.ListCreateUserView.as_view()),
    path('users/<str:user_id>/', views.ListUserDetailsView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]
