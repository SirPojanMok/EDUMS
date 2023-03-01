from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('markets:index')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):

    if request.method == "POST":

        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
                
            if user is not None:
                login(request, user)
                return redirect('markets:index')
            
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/signin.html', {'form': form})




def signout(request):

    logout(request)

    return redirect('accounts:signin')