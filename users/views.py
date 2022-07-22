from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from users.check_request_data import *


def register(request):
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        check_data = Check_Data()

        if check_data.exist_user(username):
            messages.info(request, 'This user already exists.')
        elif check_data.match_passwords(password1, password2) != True:
            messages.info(request, "Passwords doesn't match. Try again.")
        else:
            if form.is_valid():
                new_user = form.save()
                # Log the user in and then redirect to home page.
                login(request, new_user)
                return redirect('pdf2word_conv:index')
            else:
                messages.info(
                    request, 'Your password is too simple. Try another.')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
