from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetail

class UserRegisterForm(UserCreationForm):
	# email = forms.EmailField()
	mobile = forms.CharField()
	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'mobile', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	# mobile = forms.CharField()
	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'email']

class UserDetailUpdateForm(forms.ModelForm):
	class Meta:
		model = UserDetail
		fields = ['mobile','image']

	
		