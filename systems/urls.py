from django.urls import path

from .views import ListCreateSystemView, RetrieveDestroySystemView
from items.views import ListCreateItemsView


urlpatterns = [
    path("", ListCreateSystemView.as_view()),
    path("<str:pk>/", RetrieveDestroySystemView.as_view()),
    path("<str:system_id>/items/", ListCreateItemsView.as_view()),
]
