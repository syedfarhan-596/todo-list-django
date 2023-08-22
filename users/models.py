from django.db import models
from django.contrib.auth.models import User
from todo_list.models import TodoListModel
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_items = models.ForeignKey(TodoListModel,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'profile"
    