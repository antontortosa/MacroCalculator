from django.db import models
from django.forms import ModelForm


# Create your models here.
class Reg_Users(models.Model):
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

class Items(models.Model):
	name = models.CharField(max_length=30, unique="true")
	calories = models.FloatField(default=0.0)
	tot_fat = models.FloatField(default=0.0)
	tot_protein = models.FloatField(default=0.0)
	sugar = models.FloatField(default=0.0)
	tot_carbs = models.FloatField(default=0.0)
	fat_saturated = models.FloatField(default=0.0)
	fiber = models.FloatField(default=0.0)
	sodium = models.FloatField(default=0.0)
	

class Histories(models.Model):
	usuario = models.ForeignKey(Reg_Users, on_delete=models.CASCADE)
	item = models.ForeignKey(Items, on_delete=models.CASCADE)
	date_consumed = models.DateField()

class Objectives(models.Model):
	usuario = models.ForeignKey(Reg_Users, on_delete=models.CASCADE)
	calories_obj = models.IntegerField()
	carbs_obj = models.IntegerField()
	protein_obj = models.IntegerField()
	fat_obj = models.IntegerField()

class Ingredients(models.Model):
	item = models.ForeignKey(Items, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	amount = models.CharField(max_length = 15)

class ItemForm(ModelForm):
	class Meta:
		model = Items
		fields = ['name']
