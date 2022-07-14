from django.urls import path
from .views import ListCreateItemsView, RetrieveDestroyItemsView


urlpatterns = [
    path('items/', ListCreateItemsView.as_view()),
    path('items/<str:pk>/', RetrieveDestroyItemsView.as_view()),
]

