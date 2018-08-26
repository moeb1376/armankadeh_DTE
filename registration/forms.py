from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser
from django import forms


class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'phone_number']


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = UserChangeForm.Meta.fields


class MyUserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['username', 'password']
