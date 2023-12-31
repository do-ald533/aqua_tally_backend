from django.urls import path

from .views import UserDetailView, UserListView, GoalDetailView, GoalListView

urlpatterns = [
    path("", UserListView.as_view(), name="get_users"),
    path("<str:user_id>", UserDetailView.as_view(), name="get_single_user"),
    path("<str:user_id>/goals", GoalListView.as_view(), name="get_goals"),
    path("<str:user_id>/goals/<str:goal_id>", GoalDetailView.as_view(), name="single_view"),
]
