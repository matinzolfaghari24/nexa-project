from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def about(request):
    return render(request, 'store/about.html')


def contact(request):
    if request.method == 'POST':
        messages.success(request, 'پیام شما دریافت شد.')
        return redirect('store:contact')

    return render(request, 'store/contact.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('store:about')

    return render(request, 'store/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('store:about')

        messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')

    return render(request, 'store/login.html')