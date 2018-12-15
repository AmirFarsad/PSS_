from django.shortcuts import render, redirect
from accounts import models, forms
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, UpdateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import random
from django.core.mail import send_mail





# Create your views here.



class SignUpView(CreateView):
    model = models.UserModel
    
    form_class = forms.UserForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'



def ForgotPasswordView(request):
    username = request.user.username
    user = models.UserModel.objects.get(username__exact=username)
    var = 'abcdefghijklmnopqrstuvwxyzABCDEFIJKLMNOPQRSTUVWXYZ1234567890'
    confirmationcode=''
    for i in range(0,random.randrange(10,13,1)):
        c = random.choice(var)
        confirmationcode += c
    print(confirmationcode)
    send_mail(
    'کد تایید',
    '''کد تایید برای تغییر کلمه عبور شما عبارت است از
    {confirmation_code}'''.format(confirmation_code = confirmationcode),
    'alienone306@gmail.com',
    [str(user.email),],
    fail_silently=False,
    )

    user.set_password(confirmationcode)
    user.save()
    return redirect("accounts:change_password",slug = username)




def ChangePasswordView(request,slug):
    if request.method == 'POST':
        data = request.POST.copy()
        form = forms.ChangePasswordForm(data=request.POST)
        if form.is_valid():
            
            username = slug
            confirmation_code = data.get('confirmation_code')
            user = authenticate(request, username=username, password=confirmation_code)
             
            if user is not None:
                u = models.UserModel.objects.get(username__exact=username)
                u.set_password(data.get('new_password'))
                u.save()
                
                return HttpResponse("<h1>Done</h1>")
            else:
                return HttpResponse("<h1>The confirmation key you entered is not valid</h1>")
       # else:
        #    return HttpResponse("<h1>forms aren't valid</h1>")

    else:
        form = forms.ChangePasswordForm()

    return render(request,'accounts/change_password.html',{'form':form})






