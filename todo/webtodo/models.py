from django.db import models

# Create your models here.

class Task(models.Model):
	text = models.CharField(max_length=100)
	created = models.DateTimeField()
	urgency = models.IntegerField(default=1)


