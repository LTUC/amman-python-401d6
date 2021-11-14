from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
# Class based views
# Function based views


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutUsView(TemplateView):
    template_name = "about_us.html"