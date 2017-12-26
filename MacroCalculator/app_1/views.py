from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Profile, ItemForm, Ingredient, Item, History
from .forms import IngredientsForm, RegisterForm, EditProfileForm
import requests
import json
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from decimal import Decimal

def home(request):
    return render(request, 'app_1/home.html')


def index(request):
    userid = request.user.id
    return redirect('app_1:profile', user_id=userid)


def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'app_1/user_prof.html', {'user': user})


def add_food(request, user_id):
    if request.method == 'POST':  # si el usuario está enviando el formulario con datos
        form = ItemForm(request.POST)  # Bound form
        if form.is_valid():
            new_item = form.save()  # Guardar los datos en la base de datos
            url = str(new_item.id) + '/add_ingredient'
            return HttpResponseRedirect(url)
    else:
        form = ItemForm()  # Unbound form

    return render(request, 'app_1/item_form.html', {'form': form, 'user_id': user_id})

def delete_food(request, user_id, item_id):
    object = get_object_or_404(Item, pk=item_id)
    object.delete()
    return HttpResponseRedirect("/profile/" + user_id + "/history")

def add_ingredient(request, user_id, item_id):
    if request.method == 'POST':  # si el usuario está enviando el formulario con datos
        form = IngredientsForm(request.POST)  # Bound form
        if form.is_valid():

            user = Profile.objects.get(pk=user_id)
            prev_item = Item.objects.get(pk=item_id)
            calories_acum = prev_item.calories
            fat_acum = prev_item.tot_fat
            protein_acum = prev_item.tot_protein
            sugar_acum = prev_item.sugar
            carbs_acum = prev_item.tot_carbs
            sat_fat_acum = prev_item.fat_saturated
            fiber_acum = prev_item.fiber
            sodium_acum = prev_item.sodium

            app_id = "050e8e37"
            api_key = "d0142932f60a692aa1934cb8d9971206"
            url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
            headers = {'x-app-id': app_id, 'x-app-key': api_key}

            # ·INGREDIENTE 1
            val = form.cleaned_data['ingredient_1'] + ' ' + form.cleaned_data['amount_1']
            payload = {'query': val}
            consulta_raw = requests.post(url, headers=headers, data=payload).text
            consulta_dec = json.loads(consulta_raw)
            if "foods" in consulta_dec:
                calories_acum += consulta_dec["foods"][0]["nf_calories"]
                fat_acum += consulta_dec["foods"][0]["nf_total_fat"]
                protein_acum += consulta_dec["foods"][0]["nf_protein"]
                sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
                carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
                sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
                fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
                sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
                ingredient_store = Ingredient(item=prev_item, name=form.cleaned_data['ingredient_1'],
                                              amount=form.cleaned_data['amount_1'])
                ingredient_store.save()

            ingredient_ix  = "ingredient_X"
            amount_ix = "amount_x"

            for i in range(2,10):
                ingredient_ix = ingredient_ix[:-1]
                amount_ix = amount_ix[:-1]
                ingredient_ix = ingredient_ix + str(i)
                amount_ix = amount_ix + str(i)
                if form.cleaned_data[ingredient_ix] and form.cleaned_data[amount_ix]:
                    val = form.cleaned_data[ingredient_ix] + ' ' + form.cleaned_data[amount_ix]
                    payload = {'query': val}
                    consulta_raw = requests.post(url, headers=headers, data=payload).text
                    consulta_dec = json.loads(consulta_raw)
                    if "foods" in consulta_dec:
                        calories_acum += consulta_dec["foods"][0]["nf_calories"]
                        fat_acum += consulta_dec["foods"][0]["nf_total_fat"]
                        protein_acum += consulta_dec["foods"][0]["nf_protein"]
                        sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
                        carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
                        sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
                        fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
                        sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
                        ingredient_store = Ingredient(item=prev_item, name=form.cleaned_data[ingredient_ix],
                                                      amount=form.cleaned_data[amount_ix])
                        ingredient_store.save()

            prev_item.calories = calories_acum
            prev_item.tot_fat = fat_acum
            prev_item.tot_protein = protein_acum
            prev_item.sugar = sugar_acum
            prev_item.tot_carbs = carbs_acum
            prev_item.fat_saturated = sat_fat_acum
            prev_item.fiber = fiber_acum
            prev_item.sodium = sodium_acum
            prev_item.save()

            history_entry = History(usuario=user, item=prev_item, date_consumed=timezone.now())
            history_entry.save()
            return HttpResponseRedirect("/profile/" + user_id + "/history")

    else:
        form = IngredientsForm()  # Unbound form

    return render(request, 'app_1/ingredients_form.html', {'form': form, 'user_id': user_id, 'item_id': item_id})


def history(request, user_id):
    user_history = History.objects.filter(usuario=user_id)
    items_history = []
    history_entry = {}
    for entry in user_history:
        history_entry["ITEM"] = Item.objects.get(pk=entry.item_id)
        history_entry["DATE"] = entry.date_consumed
        items_history.append(history_entry)
        history_entry = {}

    context = {'items_history': items_history, 'user_id': user_id}
    return render(request, 'app_1/history.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            # username = form.cleaned_data.get('username')
            user.profile.date_birth = form.cleaned_data.get('date_birth')
            user.profile.country = form.cleaned_data.get('country')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.cp = form.cleaned_data.get('cp')
            user.profile.tags = form.cleaned_data.get('tags')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('app_1:index')
    else:
        form = RegisterForm()
    return render(request, 'app_1/register.html', {'form': form})


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
    #TODO: Mostrar formulario con los campos actuales y actualizar solo los que hayan cambiado


