from django.db import models


# Create your models here.
class signup(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __self__(self):
		return self.email 



class newsletter(models.Model):
	email = models.EmailField()

