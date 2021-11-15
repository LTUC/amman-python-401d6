from .views import ThingListView, ThingDetailView
from django.urls import path

urlpatterns = [
    path("", ThingListView.as_view(), name="things"),
    path("<int:pk>/", ThingDetailView.as_view(), name="thing_detail"),
]
