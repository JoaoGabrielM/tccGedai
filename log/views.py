from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating

def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, "login.html", {"form": form})
    return render(request, "login.html",{"form": AuthenticationForm()})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
    return render (request,"register.html",{"form": form})

@login_required
def home (request):
    return render(request, "home.html")
