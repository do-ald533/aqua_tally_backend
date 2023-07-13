import logging

import json
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from ...serializers import GoalSerializer
from ...models import GoalModel, UserModel

from ...services import calculate_goal

class GoalListView(APIView):
    logger = logging.getLogger(__name__)

    def get(self, request: Request, user_id: str) -> Response:
        user_goals = GoalModel.objects.filter(user_id=user_id)
        serializer = GoalSerializer(user_goals, many=True)
        return Response(serializer.data)
    
    def post(self, request: Request, user_id: str, format=None) -> Response:
        user = UserModel.objects.get(id=user_id)
        if not user:
            return Response(json.dumps({'data': f'User with id {user_id} does not exist'}), status.HTTP_404_NOT_FOUND)
        
        goal = calculate_goal(user)
        goal_serializer = GoalSerializer(instance=goal)
        return Response(goal_serializer.data, status=status.HTTP_201_CREATED)