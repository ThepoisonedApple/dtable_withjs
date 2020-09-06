from django.shortcuts import render,redirect
from tablodene.models import Denemetablo
from django.test import RequestFactory
from django.http import HttpResponse


from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
# Create your views here.
@login_required
@staff_member_required(view_func=None, redirect_field_name='',
                          login_url="staffonly")
def home_view(request):
	data={}
	x=Denemetablo.objects.all()
	for i in x:
		data[i.id]={
			'myint':i.rand_int,
			'mystr':i.rand_str
		}
	tmpdata={'mydata':data}
	return render(request,"home.html",tmpdata)

def reg_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method =="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form=UserCreationForm()
	return render(request,"register.html",{"form":form})

def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		return render(request, 'login.html')

def logout_wov(request):
	logout(request)
	return redirect('login')

def staffonly(request):
	logout(request)
	return render(request, 'reqlogin.html')