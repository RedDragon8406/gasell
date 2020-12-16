from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, EditUserForm, EditPfp
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            print("user login successfully")
            return redirect('/')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')
    context = {
        'title': 'ورود',
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


@transaction.atomic
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=user_name, email=email, password=password)
        user = authenticate(request, username=user_name, password=password)
        user.save()
        login(request, user)
        print("user registered,login successfully")
        return redirect('/')
    context = {
        'title': 'ثبت نام',
        'register_form': register_form
    }
    return render(request, 'account/register.html', context)


def log_out(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def user_account_main_page(request):
    update_profile = False
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if request.user.get_full_name() != "":
        update_profile = True

    context = {
        'user': user,
        'update_profile': update_profile
    }
    print(update_profile)
    return render(request, 'account/user_account_main.html', context)


@login_required(login_url='/login')
def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    edit_user_form = EditUserForm(request.POST or None,
                                  initial={
                                      'first_name': user.first_name,
                                      'last_name': user.last_name,
                                      'email': user.email,
                                      'username': user.username
                                  })

    if edit_user_form.is_valid():
        first_name = edit_user_form.cleaned_data.get('first_name')
        last_name = edit_user_form.cleaned_data.get('last_name')
        username = edit_user_form.cleaned_data.get('username')
        email = edit_user_form.cleaned_data.get('email')
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        user.save()
        return redirect('/user')

    context = {'edit_form': edit_user_form}

    return render(request, 'account/edit_account.html', context)


@login_required(login_url='/login')
def edit_user_pfp(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    edit_user_form = EditPfp(request.POST or None, request.FILES or None, initial={'pfp': user.profile.pfp})
    if edit_user_form.is_valid():
        pfp = edit_user_form.cleaned_data.get('pfp')
        user.profile.pfp = pfp
        user.save()
        return redirect('/user')

    context = {'edit_form': edit_user_form}

    return render(request, 'account/pfp_edit.html', context)


def user_sidebar(request):
    return render(request, 'account/user_sidebar.html', {})
