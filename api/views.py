from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import *
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action, permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from api.serializers import *
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import timedelta
from api.tasks import *


class UserViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin,
                  RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser,]

    @swagger_auto_schema(
        operation_summary='Forgot password',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL)
            }
        )
    )
    @action(methods=['post'], detail=False, url_path='forgot', pagination_class=None, permission_classes=[AllowAny])
    def forgot(self, request):
        email = request.data.get('email')
        if email is not None:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'Contact your system administrator'}, status=400)
            except Exception as e:
                return Response({'error': str(e)}, status=400)

            forgot_send_email.delay(user_id=user.id)
        else:
            return Response({'error': 'key "email" mandatory'}, status=400)


    @swagger_auto_schema(
        operation_summary='Login',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
            }
        ),
        responses={
            200: openapi.Response(
                description='',
                examples={
                    "application/json": {
                        "result": {
                            "user": "user@user.com",
                            "id": 1,
                            "token": "95595f53771b1da5ad881e6cc2d68e49f8dfb1d6",
                            "admin": False
                        }
                    }
                }
            ),
            401: openapi.Response(
                description='',
                examples={
                    "application/json": {
                        'result': {"error": "user not authorized"}
                    }
                }
            ),
            500: openapi.Response(
                description='',
                examples={
                    "application/json": {
                        'result': {"error": "unknown error 'MSG'"}
                    }
                }
            ),
        }
    )
    @action(methods=['post'], detail=False, url_path='login', pagination_class=None, permission_classes=[AllowAny])
    def login(self, request):
        if all([
            'username' in request.data,
            'password' in request.data
        ]):
            username = request.data['username']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'result': {'error': 'user not found'}}, status=status.HTTP_401_UNAUTHORIZED)
            except Exception as error:
                return Response({'result': {'error': f'unknown error {str(error)}'}}, status=500)

            if user.check_password(request.data.get('password')):
                token, created = Token.objects.get_or_create(user=user)

                if token.created < timezone.now() + timedelta(days=-1):
                    token.delete()
                    token = Token.objects.create(user=user)

                return Response(
                    {
                        'result': {
                            'user': user.username,
                            'id': user.id,
                            'token': token.key,
                            'admin': user.is_superuser
                        }
                    }
                )
            else:
                return Response({'result': {'error': 'user not authorized'}}, status=401)
        else:
            return Response(
                {"result": {'error': f'Required fields missing username and password'}},
                status=status.HTTP_400_BAD_REQUEST
            )
