from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Goal


class CustomLoginView(LoginView):
    template_name = 'task_base/signin.html'
    fields = '__all__'
    redirect_authenticated_user =


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
