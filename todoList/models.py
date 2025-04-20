import time

from django.db import models
from django.db.models import TextField


# Create your models here.
class Task(models.Model):
	id = time.time()
	title = models.CharField(max_length=25)
	description = models.TextField()
	done = models.BooleanField(default=False)
	
	def __str__(self):
		return self.title