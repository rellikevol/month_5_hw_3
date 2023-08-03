from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from users.models import User
from users.serializers import UserSerializer, UserDetailSerializer, UserRegisterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from users.permissions import UserPermission
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserAPIView(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['username', 'email']
    search_fields = ['username', 'email', 'first_name', 'last_name']

    def get_serializer_class(self):
        if self.action in ('retrieve',):
            return UserDetailSerializer
        if self.action in ('create',):
            return UserRegisterSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy', 'retrieve'):
            return (UserPermission(),)
        return (AllowAny(),)