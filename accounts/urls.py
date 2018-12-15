from django.urls import path,include
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView





app_name = 'accounts'


urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name = 'accounts/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('change_password_user=<slug:slug>/',views.ChangePasswordView,name = 'change_password'),
    path('forgot_password/',views.ForgotPasswordView,name = 'forgot_password'),
]
