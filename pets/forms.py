from django import forms
from django.forms import ModelForm
from .models import Pet
from usuarios.models import Usuario

class NPetForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Nombres',
			'required': '',
		}))
		
	birth = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Nombres',
			'required': '',
		}))	
		
	photo = forms.ImageField(widget=forms.TextInput(attrs={
			'type': 'file',
			'placeholder': 'Nombres',
			'required': '',
		}))	
		
	raza = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Nombres',
			'required': '',
		}))	
		
	class Meta:
		model = Pet
		exclude = ("id","usuario","estatus","estate")