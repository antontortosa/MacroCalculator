from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Profile, Item, Objective, Ingredient, History

admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Objective)
admin.site.register(Ingredient)
admin.site.register(History)