from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'deadline', 'priority', 'status')
    list_filter = ('priority', 'status', 'created_by')
    search_fields = ('title', 'description')


@admin.register(TaskImage)
class TaskImageAdmin(admin.ModelAdmin):
    list_display = ('task', 'image')


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role')  # Добавляем поля в отображение списка пользователей
    # Другие настройки админки


admin.site.register(CustomUser, CustomUserAdmin)
