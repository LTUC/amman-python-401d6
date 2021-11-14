from django.urls import path
from .views import (
                    HomePageView,
                    AboutUsView
                    )

urlpatterns=[
    path('', HomePageView.as_view(), name="home"),
    path('about-us', AboutUsView.as_view(), name="about_us")
]

