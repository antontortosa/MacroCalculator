from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    # "usuario django" con el que se asocia -> https://docs.djangoproject.com/en/1.11/ref/contrib/auth/#fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # añadir campos no presentes en User
    date_birth = models.DateField(default=None, blank=True, null=True)
    country = models.CharField(max_length=30,default=None, blank=True, null=True)
    city = models.CharField(max_length=30,default=None, blank=True, null=True)
    cp = models.IntegerField(default=None, blank=True, null=True)
    tags = models.CharField(max_length=180,default=None, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


    # def __str__(self):
    #	return self.first_name+', '+self.last_name+'\n'+self.email+'\n'+self.city+', '+str(self.cp)+'\n'+self.country


class Item(models.Model):
    name = models.CharField(max_length=30, unique="true")
    calories = models.FloatField(default=0.0)
    tot_fat = models.FloatField(default=0.0)
    tot_protein = models.FloatField(default=0.0)
    sugar = models.FloatField(default=0.0)
    tot_carbs = models.FloatField(default=0.0)
    fat_saturated = models.FloatField(default=0.0)
    fiber = models.FloatField(default=0.0)
    sodium = models.FloatField(default=0.0)


class History(models.Model):
    usuario = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_consumed = models.DateField()


class Objective(models.Model):
    usuario = models.ForeignKey(Profile, on_delete=models.CASCADE)
    calories_obj = models.IntegerField()
    carbs_obj = models.IntegerField()
    protein_obj = models.IntegerField()
    fat_obj = models.IntegerField()


class Ingredient(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.CharField(max_length = 15)

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ['name']

