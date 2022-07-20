from django.urls import path

from .views import GoalListView, GoalDetailView,GoalCreateView,GoalUpdateView,GoalDeleteView

urlpatterns = [
    path('', GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>/', GoalDetailView.as_view(), name='goal_detail'),
    path('goal_create/', GoalCreateView.as_view(), name='goal_create'),
    path('goal_update/<int:pk>/', GoalUpdateView.as_view(), name='goal_update'),
    path('goal_delete/<int:pk>/', GoalDeleteView.as_view(), name='goal_delete'),
]
