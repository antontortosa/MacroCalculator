from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Profile, Objective
from .forms import ObjectivesForm


def objective(request, user_id):
    profile = get_object_or_404(Profile, pk=user_id)

    try:
        obj = Objective.objects.get(usuario=profile)
    except Exception as e:
        obj = None

    if request.method == 'POST':
        form = ObjectivesForm(request.POST)
        if form.is_valid():
            if obj is not None:
                calories = request.POST.get('calories', obj.calories_obj)
                carbs = request.POST.get('carbs', obj.carbs_obj)
                protein = request.POST.get('protein', obj.protein_obj)
                fat = request.POST.get('fat', obj.fat_obj)

            else:
                calories = request.POST.get('calories', -1)
                carbs = request.POST.get('carbs', -1)
                protein = request.POST.get('protein',-1)
                fat = request.POST.get('fat', -1)

            obj = Objective(usuario = profile, calories_obj = calories,
                                    carbs_obj = carbs, protein_obj = protein, fat_obj = fat)
            obj.save()

    context = {'profile': profile, 'objective': obj}

    return render(request, 'app_1/user_objectives.html', context)
