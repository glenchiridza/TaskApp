from django.shortcuts import render
from django.views import generic

from .models import Goal


class GoalListView(generic.ListView):
    model = Goal
    context_object_name = 'goals'


class GoalDetailView(generic.DetailView):
    model = Goal
