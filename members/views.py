from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from store.models import Customer


"""
The 'login_user' and 'logout_user' functions are taken from the
Codemy.com tutorial referenced in the README.md but both functions
mirror the code from the Django documentation. The 'register_user'
function has been customised from the same tutorial.
"""


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Welcome back! \n' +
                                       'You have successfully logged in.'))
            return redirect('storelist')
        else:
            messages.success(request, ('There was an error logging in. \n' +
                                       'Please check your details and \n' +
                                       'try again.'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You have been successfully logged out.'))
    return redirect('store')


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = form.save()
            Customer.objects.create(user=new_user)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration succesful!'))
            return redirect('storelist')
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/register_user.html', {'form': form})
