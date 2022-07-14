from django.urls import path
from .views import ListCreateItemsView, RetrieveDestroyItemsView, ApplyBonusView, RemoveBonusView

urlpatterns = [
    path('items/', ListCreateItemsView.as_view()),
    path('items/<str:user_id>/', RetrieveDestroyItemsView.as_view()),
    path('items/<str:user_id>/apply/<str:bonus_id>/', ApplyBonusView.as_view()),
    path('items/<str:user_id>/remove/<str:bonus_id>/', RemoveBonusView.as_view())
]