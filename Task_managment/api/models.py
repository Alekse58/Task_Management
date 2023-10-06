from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    telegram_id = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=20,
                                choices=[('высокий', 'Высокий'), ('средний', 'Средний'), ('не горит', 'Не горит')])
    status = models.CharField(max_length=20, choices=[('выполнен', 'Выполнен'), ('в работе', 'В работе'),
                                                      ('простаивает', 'Простаивает')])
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks_assigned',
                                    null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks_created')


class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='task_images/')


