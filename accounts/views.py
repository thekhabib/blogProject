from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.generic import CreateView, View
from django.urls import reverse_lazy


# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class LogoutCustomView(View):
    def get(self, request):
        logout(request)
        return redirect('home_page')
