from django.urls import path
from .views import ListCreateJourneyView

urlpatterns = [
    path('systems/<str:system_id>/', ListCreateJourneyView.as_view())
]