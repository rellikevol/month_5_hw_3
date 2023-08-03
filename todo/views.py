from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from todo.models import ToDo
from todo.serializers import ToDoSerializer, ToDoCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from todo.permissions import TaskPermission
class TaskAPIView(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                  mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  GenericViewSet):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user.id)

    def get_serializer_class(self):
        if self.action in ('create',):
            return ToDoCreateSerializer
        return ToDoSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy', 'retrieve', 'list'):
            return (TaskPermission(),)
        return (IsAuthenticated(),)