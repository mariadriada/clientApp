from django.db import models

# Create your models here.
class Client(models.Model):
	id = models.AutoField(primary_key=True)
	first_name	=	models.CharField(max_length=255)
	last_name	=	models.CharField(max_length=255)
	telephon	=	models.CharField(max_length=45)
	email		=	models.EmailField()
	text	=	models.CharField(max_length=255)

	def __unicode__(self):
		return self.first_name