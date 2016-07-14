from django.shortcuts import render
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Pet
from .forms import NPetForm

class Nuevo(LoginRequiredMixin, CreateView):
	template_name = "pets/nuevo.html"
	model = Pet
	form_class = NPetForm
	success_url = '/inicio'
	def form_valid(self, form):
		form.instance.usuario = self.request.user
		return super(Nuevo, self).form_valid(form)
	def form_invalid(self, form):
		return super(Nuevo, self).form_invalid(form)
