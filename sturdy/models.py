from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Project(models.Model):
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    name = models.CharField(max_length=200)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name,)


class Task(models.Model):
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    created_date = models.DateField(auto_now=True)
    start = models.DateField(default=timezone.now)
    duration = models.DurationField(default=datetime.timedelta(days=3))
    story_points = models.PositiveIntegerField()
    value_points = models.PositiveIntegerField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        if self.parent is None:
            return '%s' % (self.title,)
        else:
            return '%s >> %s' % (self.parent, self.title,)
