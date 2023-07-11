import logging

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from ...serializers import GoalSerializer
from ...models import GoalModel, UserModel

class GoalListView(APIView):
    logger = logging.getLogger(__name__)

    def get(self, request: Request, user_id: str) -> Response:
        user_goals = GoalModel.objects.filter(user_id=user_id)
        serializer = GoalSerializer(user_goals, many=True)
        return Response(serializer.data)
    
    def post(self, request: Request, user_id: str, format=None) -> Response:
        user = UserModel.objects.get(id=user_id)
        serializer = GoalSerializer(data=request.data) # type: ignore
        if not serializer.is_valid(raise_exception=True):
            self.logger.error(serializer.error_messages)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save(user=user, goal=user.weight * 35)
        return Response(serializer.data, status=status.HTTP_201_CREATED)