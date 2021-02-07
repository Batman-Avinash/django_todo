from django.db import models


class Todo(models.Model):
    todo_status = (
        ('Complete', 'complete'),
        ('Remaining', 'remaining')
    )
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=todo_status, default='Remaining')

    def __str__(self):
        return self.title

