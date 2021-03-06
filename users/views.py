from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, NameForm, ContactusForm, UserUpdateForm
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect('myfirstapp-home')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'profile.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            subject = 'Someone contacted us.'
            content = f"""
            {first_name} {last_name} is trying to contact you.
            Their email addres is: {email}
            Message: {message}
            """
            send_mail(subject=subject, message=content,
                      from_email='test.basic90@gmail.com',
                      recipient_list=['test.basic90@gmail.com'])
            return redirect('thank_you')
    else:
        form = ContactusForm()

    return render(request, 'users/contact_us.html', {'form': form})


def thank_you(request):
    return render(request, 'users/thank_you.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {'form': form})
