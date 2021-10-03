from django.views.generic import ListView, DetailView
from .models import Thing

class ThingListView(ListView):
    template_name = "thing_list.html"
    model = Thing

class ThingDetailView(DetailView):
    template_name = "thing_detail.html"
    model = Thing
    # Add the following after showing the connection in templates
    context_object_name = 'object_things'
