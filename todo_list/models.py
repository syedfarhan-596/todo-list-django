from django.db import models

# Create your models here.
class TodoListModel(models.Model):
    item = models.CharField(max_length=120)

    def __str__(self):
        return f"item {self.id}"