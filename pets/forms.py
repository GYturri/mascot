from django import forms
from django.forms import ModelForm
from .models import Pet
from usuarios.models import Usuario

class NPetForm(forms.ModelForm):
	class Meta:
		model = Pet
		exclude = ("id","usuario","estatus","estate")