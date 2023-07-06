from django.urls import path

from .user_controller import UserController

urlpatterns = [
    path("", UserController.as_view(), name="get_users"),
    path("<str:user_id>", UserController.as_view(), name="get_single_user")
]