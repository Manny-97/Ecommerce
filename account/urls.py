from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='account/registration/login.html', form_class=UserLoginForm), name='login'),
    path('register/', views.account_registration, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
