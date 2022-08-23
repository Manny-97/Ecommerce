from dataclasses import field
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)

from .models import Customer, Address


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["full_name", "phone", "address_line", "address_line2", "town_city", "postcode"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placholder": "Full Name"}
        )
        self.fields["phone"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placholder": "Full Name"}
        )
        self.fields["address_line"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placholder": "Full Name"}
        )
        self.fields["address_line2"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placholder": "Full Name"}
        )
        self.fields["town_city"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placholder": "Full Name"}
        )
        self.fields["postcode"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placholder": "Full Name"}
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Username',
            'id': 'login-username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd'
        }
    ))


class RegistrationForm(forms.ModelForm):
    """Register User"""
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(label='Enter Email', help_text='Required', error_messages={'required': 'Sorry you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = Customer.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name

# Validate registration password
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Password do not match")
        return cd['password2']

# validate email
    def clean_email(self):
        email = self.cleaned_data['email']
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already taken, use another email")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})


class UserEditForm(forms.ModelForm):

    email = forms.CharField(
       label='Account Email (cannot be changed)', max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}
        )
    )
    user_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'Firstname': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-firstname', 'readonly': 'readonly'}
        )
    )
    first_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-lastname'}
        )
    )

    class Meta:
        model = Customer
        fields = ('email', 'user_name', 'first_name',)

    # Required fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['user_name'].required = True


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=250, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        u = Customer.objects.filter(email=email)
        if not u:
            raise forms.ValidationError("Not a User")
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'})
    )
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'})
    )
