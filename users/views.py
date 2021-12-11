
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse,reverse_lazy
from users.forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_protect
from .models import Profile
@csrf_protect
def register(request):
    context = {}
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'home/index.html')
    context['form']=form
    return render(request,'registration/register.html',context)

def profile(request,id):
    """[Profile]

    Args:
        request ([get]): [http method to retrieve data]
        id ([profile]): [retrieve specified user profile]

    Returns:
        [type]: [description]
    """
    profile = Profile.objects.get(user = id)
    return render(request,'profile.html',{"profile":profile})
