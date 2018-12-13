from django.shortcuts import render
from accounts import models, forms
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView
from django.conf import settings

# Create your views here.



class SignUpView(CreateView):
    model = models.UserModel
    
    form_class = forms.UserForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'