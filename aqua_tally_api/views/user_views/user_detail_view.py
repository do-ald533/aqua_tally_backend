from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

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
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("user_id", openapi.IN_PATH, type=openapi.FORMAT_UUID)
        ], responses={
            200: openapi.Response('OK', UserSerializer),
            404: openapi.Response('User not found')
        },
        tags=['Users']
    )
    def get(self, request: Request, user_id: str):
        try:
            user = UserModel.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except UserModel.DoesNotExist:
            return Response(
                {"error": f"User with id: {user_id} not"}, status=HTTP_404_NOT_FOUND
            )
        except ValueError:
            return Response(ValueError, status=HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
            request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'weight': openapi.Schema(type=openapi.TYPE_INTEGER)
            },
        ),
        security=[],
        tags=['Users'],
    )
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

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("user_id", openapi.IN_PATH, type=openapi.FORMAT_UUID)
        ], responses={
            204: openapi.Response('OK'),
            404: openapi.Response('User not found')
        }
    )
    def delete(self, request: Request, user_id: int) -> Response:
        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)
