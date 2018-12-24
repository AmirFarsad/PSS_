from django.shortcuts import render, redirect
from accounts import models, forms
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, UpdateView, TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import random
from django.core.mail import send_mail
from django.contrib.auth.password_validation import validate_password





# Create your views here.



class SignUpView(CreateView):
    model = models.UserModel
    
    form_class = forms.UserForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'





def ForgotPasswordView(request):
    if request.method == 'POST':
        data = request.POST.copy()
        form = forms.ConfirmationCodeForm(data=request.POST)

        if form.is_valid():
            username = data.get('username')
            try :
                user = models.UserModel.objects.get(username__exact=username)
                if user is not None:
                    var = 'abcdefghijklmnopqrstuvwxyzABCDEFIJKLMNOPQRSTUVWXYZ1234567890'
                    confirmationcode=''
                    for i in range(0,random.randrange(10,13,1)):
                        c = random.choice(var)
                        confirmationcode += c
                 
                    send_mail(
                    'کد تایید',
                    '''کد تایید برای تغییر کلمه عبور شما عبارت است از
                    {confirmation_code}'''.format(confirmation_code = confirmationcode),
                    'alienone306@gmail.com',
                    [user.email,],
                    fail_silently=False,
                    )

                    user.set_password(confirmationcode)
                    user.save()
                    return redirect("accounts:change_password",slug = username)
            except:
                error = 'نام کاربری وارد شده اشتباه است'
                return render(request,'accounts/rp_1.html',{'form':form,'error':error})
          
    else:
        form = forms.ConfirmationCodeForm()

    return render(request,'accounts/rp_1.html',{'form':form})








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
                password = data.get('new_password')
                try:
                    validate_password(password,user=u, password_validators=None)
                    u.set_password(password)               
                    u.save()
                    return redirect("accounts:success")
                except:
                    error1 ='کلمه عبور باید بیش از 6 کاراکتر باشد'
                    error2 ='کلمه عبور باید نمیتواند شامل نام کاربری باشد'
                    error3 ='کلمه عبور نمیتواند خیلی ساده باشد'
                    return render(request,'accounts/rp_2.html',{'form':form,'error1':error1,'error2':error2,'error3':error3})

            else:
                error = 'کد تایید وارد شده صحیح نمیباشد'
                return render(request,'accounts/rp_2.html',{'form':form,'error':error})
       # else:
        #    return HttpResponse("<h1>forms aren't valid</h1>")

    else:
        form = forms.ChangePasswordForm()

    return render(request,'accounts/rp_2.html',{'form':form})






class SuccessView(TemplateView):

    template_name = 'accounts/rp_success.html'


