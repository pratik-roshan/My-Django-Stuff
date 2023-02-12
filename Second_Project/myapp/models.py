from django.db import models
from datetime import datetime

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    class Meta:
        app_label = 'myapp'

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    class Meta:
        app_label = 'myapp'

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        app_label = 'myapp'

    def __str__(self):
        return str(self.date)
