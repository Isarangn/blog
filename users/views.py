from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, UserDetailUpdateForm
from .models import UserDetail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			mob = form.cleaned_data.get('mobile')
			username = form.cleaned_data.get('username')
			form.save()
			UserDetail(user=User.objects.filter(username=username).first(), mobile=mob).save()
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', {'form': form})
 

@login_required
def profile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = UserDetailUpdateForm(request.POST, request.FILES, instance=request.user.userdetail)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = UserDetailUpdateForm(instance=request.user.userdetail)


	context = {
		'u_form':u_form,
		'p_form':p_form
	}

	return render(request, 'profile.html', context)
