from datetime import datetime
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import redirect
from .forms import ContactForm
from .models import ContactSubmission
from .forms import ContactForm  # Import the ContactForm

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class AboutView(TemplateView):
    template_name = 'home/about.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

class ContactView(FormView):
    template_name = 'home/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # Save form data to the database
        submission = ContactSubmission.objects.create(
            full_name=form.cleaned_data['full_name'],
            email=form.cleaned_data['email'],
            phone_number=form.cleaned_data['phone_number'],
            message=form.cleaned_data['message']
        )
        # Redirect to success URL
        return super().form_valid(form)
class ThanksView(TemplateView):
    template_name = 'home/thanks.html'
