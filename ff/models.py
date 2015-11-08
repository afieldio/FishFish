from django.db import models
from datetime import datetime

class Events(models.Model):
	title = models.CharField(max_length=20)
	description = models.CharField(max_length=160)
	date = models.DateField()
	