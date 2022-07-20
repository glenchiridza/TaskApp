from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Goal


class CustomLoginView(LoginView):
    template_name = 'task_base/signin.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('goal_list')


class RegisterView(generic.FormView):
    template_name = 'task_base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('goal_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request.user)
        return super(RegisterView, self).form_valid(form)


class GoalCreateView(LoginRequiredMixin, generic.CreateView):
    model = Goal
    fields = ('title', 'content', 'is_complete')
    success_url = reverse_lazy('goal_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GoalCreateView, self).form_valid(form)


class GoalUpdateView(generic.UpdateView):
    model = Goal
    fields = ('title', 'content', 'is_complete')
    success_url = reverse_lazy('goal_list')


class GoalListView(LoginRequiredMixin, generic.ListView):
    model = Goal
    context_object_name = 'goals'

    def get_context_data(self, **kwargs):
        context = super(GoalListView, self).get_context_data(**kwargs)
        context['goals'] = context['goals'].filter(user=self.request.user)
        context['count'] = context['goals'].filter(is_complete=False).count()
        return context


class GoalDetailView(LoginRequiredMixin, generic.DetailView):
    model = Goal
    context_object_name = 'goal'
    template_name = 'task_base/goal_detail.html'


class GoalDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Goal
    context_object_name = 'goal'
    success_url = reverse_lazy('goal_list')
