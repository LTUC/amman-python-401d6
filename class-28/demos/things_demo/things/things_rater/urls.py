from django.urls import path
from .views import (
                        ThingCreateView,
                        ThingListView,
                        ThingDetailView,
                        ThingDeleteView,
                        ThingUpdateView
                    )


urlpatterns=[
    path('', ThingListView.as_view(), name = 'things-list'),
    path('thing/<int:pk>', ThingDetailView.as_view(), name = 'thing-detail'),
    path('create-thing/', ThingCreateView.as_view(), name = 'create-thing'),
    path('update-thing/<int:pk>', ThingUpdateView.as_view(), name = 'update-view'),
    path('delete-thing/<int:pk>', ThingDeleteView.as_view(), name = 'delete-view'),
]