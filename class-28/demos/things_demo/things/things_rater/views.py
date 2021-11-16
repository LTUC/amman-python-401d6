from typing import List
from django.db import models
from django.shortcuts import render
from django.views.generic import (
                                    ListView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                    DetailView
                                    )

from .models import Thing


class ThingListView(ListView):
    template_name = "thing_list.html"
    model = Thing
    context_object_name = 'things_list'


class ThingCreateView(CreateView):
    template_name = "thing_create.html"
    model = Thing
    fields = ['title', 'description', 'user']


class ThingDetailView(DetailView):
    template_name = "thing_detail.html"
    model = Thing
    context_object_name = 'thing'



class ThingUpdateView(UpdateView):
    template_name = "thing_update.html"
    model = Thing
    fields = ['title', 'description']


class ThingDeleteView(DeleteView):
    template_name = "thing_delete.html"
    model = Thing