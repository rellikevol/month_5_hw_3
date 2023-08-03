from rest_framework import serializers
from todo.models import ToDo
from users.models import User

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('title', 'description', 'is_completed', 'created_at', 'image')

class ToDoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('title', 'description', 'image')

    def create(self, validated_data: dict):
        user = User.objects.get(pk=self.context['request'].user.id)
        task = ToDo(
            title=validated_data['title'],
            description=validated_data['description'],
            image=validated_data['image'],
            user=user
        )
        task.save()
        return task