from django.db import models
from users.models import User


class ToDo(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    is_completed = models.BooleanField(default=False, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to='tasks_images/', default='tasks_images/default_image.png', blank=True,
                              verbose_name='Изображение')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='user_task')

    def __str__(self):
        return f"{self.user}, {self.title}, {self.created_at}, {self.is_completed}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
