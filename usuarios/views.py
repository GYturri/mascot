from django.shortcuts import render, redirect
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView
from pets.models import Pet

# Create your views here.
class Home(LoginRequiredMixin, TemplateView):
	template_name = "usuarios/home.html"
	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['usuario'] = self.request.user
		context['mascotas'] = Pet.objects.all()
		return context

# get email
def get_email(request):
	if request.method == "POST":
		request.session['saved_email'] = request.POST['email']
		backend = request.session['partial_pipeline']['backend']
		url = '/complete/%s/' % backend
		return redirect(url)
	return render(request, 'get_email.html')