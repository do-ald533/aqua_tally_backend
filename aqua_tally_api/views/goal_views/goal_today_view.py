import logging
from datetime import date

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from ...models import GoalModel, UserModel
from ...services import construct_goal_response

class GoalTodayView(APIView):
    logger = logging.getLogger(__name__)

    def get(self, request: Request, user_id: str):
        try:
            user = UserModel.objects.get(id=user_id)
            today_goal = GoalModel.objects.filter(date=date.today())
            goal_response = construct_goal_response(today_goal, user) #type: ignore
            return Response(goal_response, status=HTTP_200_OK)
        except GoalModel.DoesNotExist:
            return Response({"msg": "Goal not found"}, status=HTTP_404_NOT_FOUND)
        
    def post(self, request: Request, user_id: str):
        try:
            user = UserModel.objects.filter(id=user_id)
            
        except UserModel.DoesNotExist:
            pass