from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import sys

# Create your models here.
class Profile(models.Model):
    # "usuario django" con el que se asocia -> https://docs.djangoproject.com/en/1.11/ref/contrib/auth/#fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # añadir campos no presentes en User. No obligatorios
    date_birth = models.DateField(null=True)
    country = models.CharField(null=True, max_length=30)
    city = models.CharField(null=True, max_length=30)
    cp = models.IntegerField(null=True)
    tags = models.CharField(null=True, max_length=180)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Item(models.Model):
    name = models.CharField(max_length=30)
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
    amount = models.CharField(max_length=15)



class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name']
