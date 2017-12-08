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
            calories = request.POST.get('calories')
            obj = Objective.objects.create(usuario = profile, calories_obj = calories,
                                           carbs_obj = 0, protein_obj = 0, fat_obj = 0)
            obj.save()


    context = {'profile': profile, 'objective': obj}

    return render(request, 'app_1/user_objectives.html', context)
