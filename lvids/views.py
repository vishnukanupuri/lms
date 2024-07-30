from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Video
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
# Create your views here.
class SignupView(CreateView):
    form_class=UserCreationForm
    template_name='signup.html'
    success_url='/login'

class LogoutInterfaceView(LogoutView):
    template_name='lvids/logout.html'

class LoginInterfaceView(LoginView):
    template_name='login.html'


class Home(TemplateView):
    template_name='lvids/index.html'
    
class Dep(LoginRequiredMixin,TemplateView):
    template_name='dep.html'
    login_url='/login'
@login_required
def Cse(request):
    video = Video.objects.all()
    return render(request,'lvids/cse.html',{"video":video})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})