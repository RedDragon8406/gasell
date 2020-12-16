from django.urls import path

from .views import login_user, register, log_out, user_account_main_page, edit_user_profile, edit_user_pfp

urlpatterns = [
    path('login', login_user),
    path('logout', log_out),
    path('register', register),
    path('user', user_account_main_page),
    path('user/edit', edit_user_profile),
    path('user/edit/pfp', edit_user_pfp)
]
