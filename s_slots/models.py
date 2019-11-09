

# Create your models here.
from django.db import models

# Create your models here.
class Slot(models.Model):
	Name=models.CharField(max_length=20,default=None, unique=True)
	Monday=models.BooleanField()
	Monday_time=models.IntegerField(default=24)

	Tuesday=models.BooleanField()
	Tuesday_time=models.IntegerField(default=24)
	
	Wednesday=models.BooleanField()
	Wednesday_time=models.IntegerField(default=24)
	
	Thursday=models.BooleanField()
	Thursday_time=models.IntegerField(default=24)
	
	Friday=models.BooleanField()
	Friday_time=models.IntegerField(default=24)
	
	Saturday=models.BooleanField()
	Saturday_time=models.IntegerField(default=24)

	
