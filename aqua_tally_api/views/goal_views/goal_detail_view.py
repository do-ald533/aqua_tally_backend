import logging

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from ...serializers import GoalSerializer
from ...models import GoalModel

class GoalDetailView(APIView):
    logger = logging.getLogger(__name__)

    def patch(self, request: Request, user_id: str, goal_id: str) -> Response:
        try:
            user = GoalModel.objects.get(date=goal_id, user_id=user_id)
        except GoalModel.DoesNotExist:
            self.logger.error(f'Goal with {goal_id} and user id {user_id} doesnt exist')
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = GoalSerializer(user, data=request.data, partial=True) #type: ignore
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request: Request, user_id: int, goal_id: str) -> Response:
        try:
            user = GoalModel.objects.get(date=goal_id, user_id=user_id)
        except GoalModel.DoesNotExist:
            self.logger.error(f'goal with id: {goal_id} and user_id: {user_id} not found')
            return Response({"error": "Goal not found"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)