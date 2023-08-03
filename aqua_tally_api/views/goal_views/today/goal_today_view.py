import logging
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)

from ....models import GoalModel, UserModel
from ....serializers import GoalSerializer
from ....services import construct_goal_response
from ....validations import goal_achieved_verifier


class GoalTodayView(APIView):
    logger = logging.getLogger(__name__)

    def get(self, request: Request, user_id: str):
        try:
            user = UserModel.objects.get(id=user_id)
            today_goal = GoalModel.objects.get(date=datetime.utcnow().date(), user_id=user.id)
            if goal_achieved_verifier(today_goal, user):
                GoalModel.objects.update(goal_achieved=True)
                today_goal = GoalModel.objects.get(date=datetime.utcnow().date(), user_id=user.id)
            goal_response = construct_goal_response(today_goal, user)
            return Response(goal_response, status=HTTP_200_OK)
        except GoalModel.DoesNotExist:
            return Response({"msg": "Goal not found"}, status=HTTP_404_NOT_FOUND)
        except UserModel.DoesNotExist:
            return Response({"msg": "User not found"}, status=HTTP_404_NOT_FOUND)

    def post(self, request: Request, user_id: str):
        try:
            user = UserModel.objects.get(id=user_id)
            if GoalModel.objects.filter(date=datetime.utcnow().date(), user_id=user_id).exists():  # type: ignore
                return Response(
                    {"msg": "there can only be one Goal with the specified date"},
                    status=HTTP_400_BAD_REQUEST,
                )
            goal = GoalModel.objects.create(user=user, date=datetime.utcnow().date())  # type: ignore
            goal_response = construct_goal_response(goal, user)
            return Response(goal_response, status=HTTP_201_CREATED)

        except UserModel.DoesNotExist:
            pass
