"""Users views"""

##Django
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

##Forms
from .forms import SignUpForm, ProfileUpdateForm

def home(request):
    """Users Home View"""
    return render(request, 'home')

def signup_view(request):
    """Users SignUpView"""
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class UserEditView(generic.UpdateView):
    """Users Update data View"""
    form_class = ProfileUpdateForm
    template_name = './updateUser.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    """Users Update Password View"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')

