from django.shortcuts import render
from django.http import HttpResponseRedirect
from.forms import RegistrationForm
# Create your views here.
def index(request):
    return render(request,'./page/home.html')
def register(request):
    form = RegistrationForm()
    if request.method =='POST':

        form  = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'page/register.html',{'form': form})