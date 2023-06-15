from rest_framework import mixins, permissions, viewsets

from .serializers import UserSerializer


class UserViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
