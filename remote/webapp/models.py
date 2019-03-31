from django.db import models

# Create your models here.
class employee(models.Model):
	"""docstring for employee"""
	firstname= models.CharField(max_length = 10)
	lastname = models.CharField(max_length=10)
	emp_id = models.IntegerField()

	def __str__(self):
		return self.firstname

class command(models.Model):
	task = models.CharField(max_length = 100)
	done = models.CharField(max_length = 10,default="false")

	def __str__(self):
		return self.task

	
		
		

