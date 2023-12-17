from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):

    if request.user.is_authenticated:
        return redirect('index_page')

    if request.method == 'POST':
        form = UserLoginForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('index_page')
            else:
                return render(request, 'login.html', {
                    'form': form,
                })
        else:
            return render(request, 'login.html', {
                'form': form,
            })
    else:

        form = UserLoginForm()
        return render(request, 'login.html', {
            'form': form,
        })