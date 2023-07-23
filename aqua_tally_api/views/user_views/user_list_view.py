import logging
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from ...services import calculate_goal

from ...serializers import UserSerializer
from ...models import UserModel

class UserListView(APIView, LimitOffsetPagination):
    logger = logging.getLogger(__name__)

    @swagger_auto_schema(
        query_serializer=UserSerializer,
        responses={200: UserSerializer(many=True)},
        tags=['Users'],
    )
    def get(self, request: Request) -> Response:
        users = UserModel.objects.all()
        results = self.paginate_queryset(users, request, view=self)
        serializer = UserSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

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
    def post(self, request: Request) -> Response | None:
        try:
            name = request.data.get('name') #type: ignore
            weight = request.data.get('weight') #type: ignore
            if not name or not weight:
                return Response({"msg": "missing informations"}, status=HTTP_400_BAD_REQUEST)

            goal = calculate_goal(float(weight))
            user = UserModel.objects.create(name=name, weight=weight, goal=goal)
            user_serializer = UserSerializer(instance=user)
            return Response(user_serializer.data, status=HTTP_201_CREATED)
        except Exception:
            self.logger.error(f"Unexpected error occured {Exception}")
