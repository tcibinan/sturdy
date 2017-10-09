from django.db import models

# Create your models here.
class Project(models.Model):
    class Meta:
        verbose_name = 'Команда'

    name = models.CharField(max_length = 200)
    created_date = models.DateField(auto_now = True)

class Task(models.Model):
    class Meta:
        verbose_name = 'Задание'

    title = models.CharField(max_length = 200)
    description = models.TextField()
    created_date = models.DateField(auto_now = True)
    story_points = models.PositiveIntegerField()
    value_points = models.PositiveIntegerField()
    project = models.ForeignKey(
        Project,
        on_delete = models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
    )