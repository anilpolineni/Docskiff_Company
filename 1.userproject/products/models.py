from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Items(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=20)
	cost=models.DecimalField(decimal_places=2, max_digits=6)
	model=models.CharField(max_length=100)


	def __str__(self):
		return self.user.username


