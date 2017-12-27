from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import History, Profile, Item
import requests
import json
import sys

class ItemForm(forms.Form):
    name = forms.CharField(label='Name', max_length = 100,required=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # cache the user object you pass in
        super(ItemForm, self).__init__(*args, **kwargs)  # and carry on to init the form


    def clean(self):
    # test the rate limit by passing in the cached user object
        cleaned_data = super().clean()
        name_form = cleaned_data.get('name')
        myHistory = History.objects.filter(usuario=Profile.objects.get(pk=self.user))
        l_items = myHistory.values_list()
        #print("XXXXXXXXXXXXXXXXXXXXXX", file=sys.stderr)
        #print(l_items, file=sys.stderr)
        #print("XXXXXXXXXXXXXXXXXXXXXX", file=sys.stderr)
        for ll in l_items :
            if name_form == Item.objects.get(pk=ll[2]).name :
                ##ERROR
                raise forms.ValidationError(
                        "Food name "+ cleaned_data["name"] +" already exists"
                )
        return self.cleaned_data  # never forget this!

class IngredientsForm(forms.Form):
    ingredient_1 = forms.CharField(label='Ingredient 1', max_length=100,required=True)
    amount_1 = forms.CharField(label='Amount 1', max_length=100,required=True)
    ingredient_2 = forms.CharField(label='Ingredient 2', max_length=100,required=False)
    amount_2 = forms.CharField(label='Amount 2', max_length=100,required=False)
    ingredient_3 = forms.CharField(label='Ingredient 3', max_length=100,required=False)
    amount_3 = forms.CharField(label='Amount 3', max_length=100,required=False)
    ingredient_4 = forms.CharField(label='Ingredient 4', max_length=100,required=False)
    amount_4 = forms.CharField(label='Amount 4', max_length=100,required=False)
    ingredient_5 = forms.CharField(label='Ingredient 5', max_length=100,required=False)
    amount_5 = forms.CharField(label='Amount 5', max_length=100,required=False)
    ingredient_6 = forms.CharField(label='Ingredient 6', max_length=100,required=False)
    amount_6 = forms.CharField(label='Amount 6', max_length=100,required=False)
    ingredient_7 = forms.CharField(label='Ingredient 7', max_length=100,required=False)
    amount_7 = forms.CharField(label='Amount 7', max_length=100,required=False)
    ingredient_8 = forms.CharField(label='Ingredient 8', max_length=100,required=False)
    amount_8 = forms.CharField(label='Amount 8', max_length=100,required=False)
    ingredient_9 = forms.CharField(label='Ingredient 9', max_length=100,required=False)
    amount_9 = forms.CharField(label='Amount 9', max_length=100,required=False)
    ingredient_10 = forms.CharField(label='Ingredient 10', max_length=100,required=False)
    amount_10 = forms.CharField(label='Amount 10', max_length=100,required=False)

    def clean(self):
        form_data = self.cleaned_data
        #Set API
        app_id = "050e8e37"
        api_key = "d0142932f60a692aa1934cb8d9971206"
        url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
        headers = {'x-app-id': app_id, 'x-app-key': api_key}
        #Call API
        
        ingredient_ix  = "ingredient_X"
        amount_ix = "amount_X"

        for i in range(1,10):
            ingredient_ix = ingredient_ix[:-1]
            ingredient_ix = ingredient_ix + str(i)
            amount_ix = amount_ix[:-1]
            amount_ix = amount_ix + str(i)
            if form_data[ingredient_ix] :
                val = form_data[ingredient_ix] + ' ' + form_data[amount_ix]
                if val != "" :
                    payload = {'query': val}
                    consulta_raw = requests.post(url, headers=headers, data=payload).text
                    consulta_dec = json.loads(consulta_raw)
                    #   
                    if "message" in consulta_dec and consulta_dec['message'] == "We couldn't match any of your foods" :
                        raise forms.ValidationError(
                            "Ingredient "+str(i)+" doesn't match any known ingredient"
                        )

        return form_data



class ObjectivesForm(forms.Form):
    calories = forms.IntegerField(label="calories", max_value=15000, required=True)


class RegisterForm(UserCreationForm):
    date_birth = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    country = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    cp = forms.IntegerField(help_text='Zip code')
    tags = forms.CharField(max_length=180)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class EditProfileForm(forms.Form):
    #user = instance.id
    #TODO: ver cómo poner valores iniciales
    date_birth = forms.DateField()
    country = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    cp = forms.IntegerField()
    tags = forms.CharField(max_length=180)

