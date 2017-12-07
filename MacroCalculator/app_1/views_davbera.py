from django.shortcuts import get_object_or_404, render

from .models import Profile, Objective



def objective(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    obj = get_object_or_404(Objective, pk=user_id)
    return render(request, 'app_1/user_objectives.html', {'user': user, 'objective': obj})