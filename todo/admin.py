from django.contrib import admin
from todo.models import ToDo
# Register your models here.
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at', 'is_completed')
    search_fields = ('user', 'title', 'created_at', 'is_completed')