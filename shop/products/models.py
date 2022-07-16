from django.db import models
from django.utils import timezone
# Create your models here.


class Products(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	stocks = models.IntegerField(default=0)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	description = models.TextField()
	discount = models.IntegerField(default=0)
	image = models.ImageField(upload_to='media/')
	date = models.DateTimeField(default=timezone.now)




	def __str__(self):
		return self.name



class Category(models.Model):
	name = models.CharField(max_length=200)


	def __str__(self):
		return self.name