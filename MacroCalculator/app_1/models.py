from django.db import models

# Create your models here.
class Reg_User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	date_birth = models.DateField()
	country = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	cp = models.IntegerField()
	tags = models.CharField(max_length=180)

	def __str__(self):
		return self.first_name+', '+self.last_name+'\n'+self.email+'\n'+self.city+', '+str(self.cp)+'\n'+self.country

class Item(models.Model):
	calories = models.FloatField()
	tot_fat = models.FloatField()
	tot_protein = models.FloatField()
	sugar = models.FloatField()
	tot_carbs = models.FloatField()
	fat_saturated = models.FloatField()
	fiber = models.FloatField()
	sodium = models.FloatField()
	name = models.CharField(max_length=30)

class Histories(models.Model):
	usuario = models.ForeignKey(Reg_User, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	date_consumed = models.DateField()

class Objectives(models.Model):
	usuario = models.ForeignKey(Reg_User, on_delete=models.CASCADE)
	calories_obj = models.IntegerField()
	carbs_obj = models.IntegerField()
	protein_obj = models.IntegerField()
	fat_obj = models.IntegerField()

class Ingredients(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	amount = models.CharField(max_length = 15)