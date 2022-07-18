from django.urls import path

from .views import ListCreateCharView, CharDetailsView, AlterStatusView, GainExpView, UpgradeCharView , AddNewItemToInventoryView

urlpatterns = [
    path("", ListCreateCharView.as_view()),
    path("<str:pk>/", CharDetailsView.as_view()),
    path("<str:pk>/change-status/", AlterStatusView.as_view()),
    path("<str:pk>/stats/", UpgradeCharView.as_view()),
    path("<str:pk>/exp/", GainExpView.as_view()),
    path("<str:char_id>/inventory/add/<str:item_id>/", AddNewItemToInventoryView.as_view())
]