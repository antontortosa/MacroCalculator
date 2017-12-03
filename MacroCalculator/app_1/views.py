from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Reg_User

def index(request):
    all_users = Reg_User.objects.all()
    context = {'all_users':all_users}
    return render(request, 'app_1/index.html', context)


def reg_user(request, user_id):
    user = get_object_or_404(Reg_User, pk=user_id)
    return render(request, 'app_1/user_prof.html',{'user':user})

def history(request, user_id):
    response = "You're looking at the history of user %s."
    return HttpResponse(response % user_id)