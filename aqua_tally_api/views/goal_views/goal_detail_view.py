import logging

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from ...serializers import GoalSerializer
from ...models import GoalModel

class GoalDetailView(APIView):
    logger = logging.getLogger(__name__)

    def get(self, request: Request, user_id: str, goal_id: str):
        try:
            goal = GoalModel.objects.get(id=goal_id, user_id=user_id)
            serializer = GoalSerializer(goal)
            return Response(serializer.data)
        except GoalModel.DoesNotExist:
            return Response(
                {"error": f"User with id: {user_id} not"}, status=HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response(ValueError, status=HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, user_id: str, goal_id: str) -> Response:
        try:
            user = GoalModel.objects.get(id=goal_id, user_id=user_id)
            serializer = GoalSerializer(user, data=request.data, partial=True) #type: ignore
            if not serializer.is_valid():
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data)
        except GoalModel.DoesNotExist:
            self.logger.error(f'Goal with {goal_id} and user id {user_id} doesnt exist')
            return Response({"error": "User not found"}, status=HTTP_404_NOT_FOUND)

    
    def delete(self, request: Request, user_id: int, goal_id: str) -> Response:
        try:
            goal = GoalModel.objects.get(id=goal_id, user_id=user_id)
            goal.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except GoalModel.DoesNotExist:
            self.logger.error(f'goal with id: {goal_id} and user_id: {user_id} not found')
            return Response({"error": "Goal not found"}, status=HTTP_404_NOT_FOUND)
