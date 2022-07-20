from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Goal


class GoalCreateView(generic.CreateView):
    model = Goal
    fields = "__all__"
    success_url = reverse_lazy('goal_list')


class GoalUpdateView(generic.UpdateView):
    model = Goal
    fields = "__all__"
    success_url = reverse_lazy('goal_list')


class GoalListView(generic.ListView):
    model = Goal
    context_object_name = 'goals'


class GoalDetailView(generic.DetailView):
    model = Goal
    context_object_name = 'goal'
    template_name = 'task_base/goal_detail.html'


class GoalDeleteView(generic.DeleteView):
    model = Goal
    context_object_name = 'goal'
    success_url = reverse_lazy('goal_list')
