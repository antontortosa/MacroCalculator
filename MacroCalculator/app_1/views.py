from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import Profile, ItemForm, Ingredients, Items, Histories
from .forms import IngredientsForm, RegisterForm
import requests
import json
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'app_1/home.html')


def index(request):
    all_users = Profile.objects.all()
    context = {'all_users': all_users}
    return render(request, 'app_1/index.html', context)


def profile(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    return render(request, 'app_1/user_prof.html', {'user': user})


def add_food(request, user_id):
    if request.method == 'POST':  # si el usuario está enviando el formulario con datos
        form = ItemForm(request.POST)  # Bound form
        if form.is_valid():
            new_item = form.save() #Guardar los datos en la base de datos
            url = str(new_item.id) + '/add_ingredient'
            return HttpResponseRedirect(url)
    else:
        form = ItemForm() #Unbound form

    return render(request, 'app_1/item_form.html', {'form': form, 'user_id':user_id})


def add_ingredient(request, user_id, item_id):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = IngredientsForm(request.POST) #Bound form
        if form.is_valid():

            user = Profile.objects.get(pk=user_id)
            prev_item = Items.objects.get(pk=item_id)
            calories_acum = prev_item.calories
            fat_acum = prev_item.tot_fat
            protein_acum = prev_item.tot_protein
            sugar_acum = prev_item.sugar
            carbs_acum = prev_item.tot_carbs
            sat_fat_acum = prev_item.fat_saturated
            fiber_acum = prev_item.fiber
            sodium_acum = prev_item.sodium

            app_id="050e8e37"
            api_key="d0142932f60a692aa1934cb8d9971206"
            url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
            headers = {'x-app-id': app_id, 'x-app-key': api_key}

            #·INGREDIENTE 1
            val = form.cleaned_data['ingredient_1'] +' '+ form.cleaned_data['amount_1']
            payload = {'query': val}
            consulta_raw = requests.post(url, headers=headers, data=payload).text
            consulta_dec = json.loads(consulta_raw)
            calories_acum += consulta_dec["foods"][0]["nf_calories"]
            fat_acum += consulta_dec["foods"][0]["nf_total_fat"]
            protein_acum += consulta_dec["foods"][0]["nf_protein"]
            sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
            carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
            sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
            fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
            sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
            ingredient_store = Ingredients(item=prev_item, name=form.cleaned_data['ingredient_1'], amount=form.cleaned_data['amount_1'])
            ingredient_store.save()

            #·INGREDIENTE 2
            if form.cleaned_data['ingredient_2'] and form.cleaned_data['amount_2'] :
                val = form.cleaned_data['ingredient_2'] +' '+ form.cleaned_data['amount_2']
                payload = {'query': val}
                consulta_raw = requests.post(url, headers=headers, data=payload).text
                consulta_dec = json.loads(consulta_raw)
                calories_acum += consulta_dec["foods"][0]["nf_calories"]
                fat_acum += consulta_dec["foods"][0]["nf_total_fat"]
                protein_acum += consulta_dec["foods"][0]["nf_protein"]
                sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
                carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
                sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
                fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
                sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
                ingredient_store = Ingredients(item=prev_item, name=form.cleaned_data['ingredient_2'], amount=form.cleaned_data['amount_2'])
                ingredient_store.save()

            #·INGREDIENTE 3
            if form.cleaned_data['ingredient_3'] and form.cleaned_data['amount_3'] :
                val = form.cleaned_data['ingredient_3'] +' '+ form.cleaned_data['amount_3']
                payload = {'query': val}
                consulta_raw = requests.post(url, headers=headers, data=payload).text
                consulta_dec = json.loads(consulta_raw)
                calories_acum += consulta_dec["foods"][0]["nf_calories"]
                fat_acum += consulta_dec["foods"][0]["nf_total_fat"]
                protein_acum += consulta_dec["foods"][0]["nf_protein"]
                sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
                carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
                sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
                fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
                sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
                ingredient_store = Ingredients(item=prev_item, name=form.cleaned_data['ingredient_3'], amount=form.cleaned_data['amount_3'])
                ingredient_store.save()

            #INGREDIENTE 4
            if form.cleaned_data['ingredient_4'] and form.cleaned_data['amount_4'] :
                val = form.cleaned_data['ingredient_4'] +' '+ form.cleaned_data['amount_4']
                payload = {'query': val}
                consulta_raw = requests.post(url, headers=headers, data=payload).text
                consulta_dec = json.loads(consulta_raw)
                calories_acum += consulta_dec["foods"][0]["nf_calories"]
                fat_acum += consulta_dec["foods"][0]["nf_total_fat"]
                protein_acum += consulta_dec["foods"][0]["nf_protein"]
                sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
                carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
                sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
                fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
                sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
                ingredient_store = Ingredients(item=prev_item, name=form.cleaned_data['ingredient_4'], amount=form.cleaned_data['amount_4'])
                ingredient_store.save()

            #INGREDIENTE 5
            if form.cleaned_data['ingredient_5'] and form.cleaned_data['amount_5'] :
                val = form.cleaned_data['ingredient_5'] +' '+ form.cleaned_data['amount_5']
                payload = {'query': val}
                consulta_raw = requests.post(url, headers=headers, data=payload).text
                consulta_dec = json.loads(consulta_raw)
                calories_acum += consulta_dec["foods"][0]["nf_calories"]
                fat_acum += consulta_dec["foods"][0]["nf_total_fat"]
                protein_acum += consulta_dec["foods"][0]["nf_protein"]
                sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
                carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
                sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
                fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
                sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
                ingredient_store = Ingredients(item=prev_item, name=form.cleaned_data['ingredient_5'], amount=form.cleaned_data['amount_5'])
                ingredient_store.save()

            # INGREDIENTE 6
            if form.cleaned_data['ingredient_6'] and form.cleaned_data['amount_6'] :
                val = form.cleaned_data['ingredient_6'] +' '+ form.cleaned_data['amount_6']
                payload = {'query': val}
                consulta_raw = requests.post(url, headers=headers, data=payload).text
                consulta_dec = json.loads(consulta_raw)
                calories_acum += consulta_dec["foods"][0]["nf_calories"]
                fat_acum += consulta_dec["foods"][0]["nf_total_fat"]
                protein_acum += consulta_dec["foods"][0]["nf_protein"]
                sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
                carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
                sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
                fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
                sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
                ingredient_store = Ingredients(item=prev_item, name=form.cleaned_data['ingredient_6'], amount=form.cleaned_data['amount_6'])
                ingredient_store.save()

            #INGREDIENTE 7
            if form.cleaned_data['ingredient_7'] and form.cleaned_data['amount_7']:
                val = form.cleaned_data['ingredient_7'] +' '+ form.cleaned_data['amount_7']
                payload = {'query': val}
                consulta_raw = requests.post(url, headers=headers, data=payload).text
                consulta_dec = json.loads(consulta_raw)
                calories_acum += consulta_dec["foods"][0]["nf_calories"]
                fat_acum += ["foods"][0]["nf_total_fat"]
                protein_acum += consulta_dec["foods"][0]["nf_protein"]
                sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
                carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
                sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
                fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
                sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
                ingredient_store = Ingredients(item=prev_item, name=form.cleaned_data['ingredient_7'], amount=form.cleaned_data['amount_7'])
                ingredient_store.save()

            #INGREDIENTE 8
            if form.cleaned_data['ingredient_8'] and form.cleaned_data['amount_8'] :
                val = form.cleaned_data['ingredient_8'] +' '+ form.cleaned_data['amount_8']
                payload = {'query': val}
                consulta_raw = requests.post(url, headers=headers, data=payload).text
                consulta_dec = json.loads(consulta_raw)
                calories_acum += consulta_dec["foods"][0]["nf_calories"]
                fat_acum += consulta_dec["foods"][0]["nf_total_fat"]
                protein_acum += consulta_dec["foods"][0]["nf_protein"]
                sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
                carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
                sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
                fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
                sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
                ingredient_store = Ingredients(item=prev_item, name=form.cleaned_data['ingredient_8'], amount=form.cleaned_data['amount_8'])
                ingredient_store.save()

            #INGREDIENTE 9
            if form.cleaned_data['ingredient_9'] and form.cleaned_data['amount_9'] :
                val = form.cleaned_data['ingredient_9'] +' '+ form.cleaned_data['amount_9']
                payload = {'query': val}
                consulta_raw = requests.post(url, headers=headers, data=payload).text
                consulta_dec = json.loads(consulta_raw)
                calories_acum += consulta_dec["foods"][0]["nf_calories"]
                fat_acum += consulta_dec["foods"][0]["nf_total_fat"]
                protein_acum += consulta_dec["foods"][0]["nf_protein"]
                sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
                carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
                sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
                fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
                sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
                ingredient_store = Ingredients(item=prev_item, name=form.cleaned_data['ingredient_9'], amount=form.cleaned_data['amount_9'])
                ingredient_store.save()

            #INGREDIENTE 10
            if form.cleaned_data['ingredient_10'] and form.cleaned_data['amount_10'] :
                val = form.cleaned_data['ingredient_10'] +' '+ form.cleaned_data['amount_10']
                payload = {'query': val}
                consulta_raw = requests.post(url, headers=headers, data=payload).text
                consulta_dec = json.loads(consulta_raw)
                calories_acum += consulta_dec["foods"][0]["nf_calories"]
                fat_acum += consulta_dec["foods"][0]["nf_total_fat"]
                protein_acum += consulta_dec["foods"][0]["nf_protein"]
                sugar_acum += consulta_dec["foods"][0]["nf_sugars"]
                carbs_acum += consulta_dec["foods"][0]["nf_total_carbohydrate"]
                sat_fat_acum += consulta_dec["foods"][0]["nf_saturated_fat"]
                fiber_acum += consulta_dec["foods"][0]["nf_dietary_fiber"]
                sodium_acum += consulta_dec["foods"][0]["nf_sodium"]
                ingredient_store = Ingredients(item=prev_item, name=form.cleaned_data['ingredient_10'], amount=form.cleaned_data['amount_10'])
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

            history_entry = Histories(usuario=user, item=prev_item, date_consumed=timezone.now())
            history_entry.save()
            return HttpResponseRedirect("/app_1/profile/"+user_id+"/history")

    else:
        form = IngredientsForm() # Unbound form

    return render(request, 'app_1/ingredients_form.html', {'form': form, 'user_id':user_id,'item_id':item_id })


def history(request, user_id):
    response = "You're looking at the history of user %s."
    return HttpResponse(response % user_id)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            #username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('app_1:profile') # cuando esté, que redirija a la página del perfil
    else:
        form = RegisterForm()
    return render(request, 'app_1/register.html', {'form': form})
