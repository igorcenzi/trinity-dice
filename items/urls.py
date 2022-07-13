from django.urls import path
from .views import ListCreateItemsView, RetrieveDestroyItemsView


urlpatterns = [
    path('', ListCreateItemsView.as_view()),
    path('<str:pk>/', RetrieveDestroyItemsView.as_view()),
]

