from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("bonus/", include("bonus.urls")),
    path("items/", include("items.urls")),
    path("systems/", include("systems.urls")),
    path("", include("classes.urls")),
]
