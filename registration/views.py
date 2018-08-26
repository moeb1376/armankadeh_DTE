from django.shortcuts import render, redirect
from .forms import MyUserCreationForm, MyUserLoginForm
from django.contrib.auth import authenticate, login as user_login
from .models import MyUser
from .decorators import check_recaptcha


def index(request):
    return render(request, 'index.html')


def forgot_password(request):
    return render(request, 'registration/password_reset_form.html')


@check_recaptcha
def login_register(request):
    if request.method == 'POST':
        if request.POST['state'] == 'login':
            login_form = MyUserLoginForm(request.POST)
            logged_in = False
            user = None
            if request.recaptcha_is_valid:
                if login_form.is_valid():
                    username = login_form.cleaned_data['username']
                    password = login_form.cleaned_data['password']
                    user = MyUser.objects.get(username=username)
                    if user.check_password(password):
                        user_login(request, user)
                        logged_in = True
                if user and logged_in:
                    return redirect('index')
                else:
                    register_form = MyUserCreationForm()
                    login_form.add_error('__all__',
                                         'Please enter a correct username and password. Note that both fields may be case-sensitive.')
                    return render(request, 'registration/login_register.html',
                                  {'login_form': login_form, 'register_form': register_form})
            else:
                register_form = MyUserCreationForm()
                login_form.add_error('__all__',
                                     'Check reCAPTCHA!')
                return render(request, 'registration/login_register.html',
                              {'login_form': login_form, 'register_form': register_form})
        else:
            register_form = MyUserCreationForm(request.POST)
            user = None
            if request.recaptcha_is_valid:
                if register_form.is_valid():
                    register_form.save()
                    user = authenticate(first_name=register_form.cleaned_data['first_name'],
                                        last_name=register_form.cleaned_data['last_name'],
                                        username=register_form.cleaned_data['username'],
                                        password=register_form.cleaned_data['password1'],
                                        email=register_form.cleaned_data['email'],
                                        phone_number=register_form.cleaned_data['phone_number'])
                    user_login(request, user)
                if user:
                    return redirect('index')
                else:
                    login_form = MyUserLoginForm()
                    return render(request, 'registration/login_register.html',
                                  {'login_form': login_form, 'register_form': register_form})
            else:
                login_form = MyUserLoginForm()
                register_form.add_error('__all__',
                                     'Check reCAPTCHA!')
                return render(request, 'registration/login_register.html',
                              {'login_form': login_form, 'register_form': register_form})
    else:
        login_form = MyUserLoginForm()
        register_form = MyUserCreationForm()
        return render(request, 'registration/login_register.html',
                      {'login_form': login_form, 'register_form': register_form})

