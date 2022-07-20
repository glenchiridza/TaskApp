from django.urls import path

from .views import (GoalListView, GoalDetailView,GoalCreateView,
                    GoalUpdateView,GoalDeleteView,CustomLoginView)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>/', GoalDetailView.as_view(), name='goal_detail'),
    path('goal_create/', GoalCreateView.as_view(), name='goal_create'),
    path('goal_update/<int:pk>/', GoalUpdateView.as_view(), name='goal_update'),
    path('goal_delete/<int:pk>/', GoalDeleteView.as_view(), name='goal_delete'),
]
