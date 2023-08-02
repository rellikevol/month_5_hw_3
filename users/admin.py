from django.contrib import admin
from users.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'date_joined')