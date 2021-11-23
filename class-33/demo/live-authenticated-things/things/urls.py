from django.urls import path
from .views import ThingList, ThingDetail

urlpatterns = [
    path('', ThingList.as_view(), name='thing-list'),
    path('<int:pk>/', ThingDetail.as_view(), name='thing-detail'),
]