import logging

import json
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from ...serializers import GoalSerializer
from ...models import GoalModel, UserModel

from ...services import calculate_goal
from ...validations import validate_date


class GoalListView(APIView, LimitOffsetPagination):
    logger = logging.getLogger(__name__)

    def get(self, request: Request, user_id: str) -> Response:
        user_goals = GoalModel.objects.filter(user_id=user_id)
        results = self.paginate_queryset(user_goals, request, view=self)
        serializer = GoalSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request, user_id: str) -> Response:
        try:
            user = UserModel.objects.get(id=user_id)

            calculated_goal = calculate_goal(user)
            if request.data.get("date") and validate_date(request.data.get("date")):  # type: ignore
                if GoalModel.objects.filter(date=request.data.get("date"), user_id=user_id).exists():  # type: ignore
                    return Response(
                        {"msg": "there can only be one Goal with the specified date"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                goal = GoalModel.objects.create(user=user, goal=calculated_goal, date=request.data.get("date"))  # type: ignore
                goal_serializer = GoalSerializer(instance=goal)
                return Response(goal_serializer.data, status=status.HTTP_201_CREATED)

            return Response(
                {"msg": f"the date provided is a date that already passed"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except UserModel.DoesNotExist:
            return Response(
                {"msg": f"User with id {user_id} does not exist"},
                status.HTTP_404_NOT_FOUND,
            )
