from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
)

from ...serializers import UserSerializer
from ...models import UserModel


class UserDetailView(APIView):
    """
    list, update or delete a single user view
    """

    def get(self, request: Request, user_id):
        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request: Request, user_id: str) -> Response:
        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)  # type: ignore
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, user_id: int) -> Response:
        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)
