import logging
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from ....models import GoalModel, UserModel
from ....serializers import GoalSerializer
from ....services import construct_goal_response
from ....validations import goal_achieved_verifier

class GoalDateView(APIView):
    logger = logging.getLogger(__name__)

    def get(self, request: Request, user_id: str, date: str):
        try:
            valid_date = datetime.fromisoformat(date)
            user = UserModel.objects.get(id=user_id)
            today_goal = GoalModel.objects.get(date=valid_date, user_id=user.id)
            goal_response = construct_goal_response(today_goal, user)
            return Response(goal_response, status=HTTP_200_OK)
        except GoalModel.DoesNotExist:
            return Response({"msg": "Goal not found"}, status=HTTP_404_NOT_FOUND)
        except UserModel.DoesNotExist:
            return Response({"msg": "User not found"}, status=HTTP_404_NOT_FOUND)