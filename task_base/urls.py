from django.urls import path

from .views import GoalListView, GoalDetailView,GoalCreateView

urlpatterns = [
    path('', GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>/', GoalDetailView.as_view(), name='goal_detail'),
    path('goal_create/', GoalCreateView.as_view(), name='goal_create'),
]
