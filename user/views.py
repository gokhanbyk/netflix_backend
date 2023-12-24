from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from .models import *

# Create your views here.
def login_view(request):

    if request.user.is_authenticated:
        return redirect('profile_page')

    if request.method == 'POST':
        form = UserLoginForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('profile_page')
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
    


def register_view(request):

    if request.user.is_authenticated:
        return redirect('profile_page')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            # return redirect('login_page')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect('profile_page')
        else:
            return render(request, 'register.html', {
                'form': form
            })

    form = UserRegisterForm()
    return render(request, 'register.html', {
        'form': form
    })



def profile_page_view(request):


    profiles = Profile.objects.filter(user = request.user)

    return render(request, 'profile_view.html', {
        'profiles': profiles
    })


def profile_add_view(request):

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_page')
        else:
            return render(request, 'profile_add.html', {
                'form': form
            })

    form = UserProfileForm()
    return render(request, 'profile_add.html', {
        'form': form
    })


def profile_edit_view(request, profile_slug):

    profile = Profile.objects.get(slug = profile_slug)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('profile_page')
    else:
        form = UserProfileForm(instance=profile)
        return render(request, 'profile_edit.html', {
            'form': form
        })
    

def profile_delete_view(request, profile_slug):

    profile = Profile.objects.get(slug = profile_slug)
    
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_page')
    else:
        return render(request, 'profile_delete.html', {
            'profile': profile
        })