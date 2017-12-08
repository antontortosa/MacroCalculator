from django.shortcuts import get_object_or_404, render

from .models import Profile, Objective



def objective(request, user_id):
    profile = get_object_or_404(Profile, pk=user_id)
    obj = None
    #obj = Objective.objects.get(usuario=user)

    context = {'profile': profile, 'objective': obj}
    return render(request, 'app_1/user_objectives.html', context)
