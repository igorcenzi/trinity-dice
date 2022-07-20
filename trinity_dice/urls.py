from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("bonus/", include("bonus.urls")),
    path("items/", include("items.urls")),
    path("systems/", include("systems.urls")),
    path("classes/", include("classes.urls")),
    path("journeys/", include("journeys.urls")),
    path("characters/", include("characters.urls")),
    path("login/", TokenObtainPairView.as_view()),
]
