from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Profile, Objective
from .forms import ObjectivesForm


def objective(request, user_id):
    if request.method == 'POST':
        form = ObjectivesForm(request.POST)
        if form.is_valid():
            return HttpResponse("Se ha recibido POST valido")
        else:
            return HttpResponse("EL formulario recibido no es valido")

    profile = get_object_or_404(Profile, pk=user_id)
    obj = None
    #obj = Objective.objects.get(usuario=user)

    context = {'profile': profile, 'objective': obj}

    return render(request, 'app_1/user_objectives.html', context)
