from django.db import models

# Create your models here.
class personal(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField('date published')
	boy= models.BooleanField(default = 0)
	def __str__(self):
		return self.name
