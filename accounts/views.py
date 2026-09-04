from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect_by_role(request.user)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect_by_role(user)

        messages.error(
            request,
            "Username atau password salah."
        )

    return render(
        request,
        "accounts/login.html"
    )


def logout_view(request):
    logout(request)
    return redirect("login")


def redirect_by_role(user):

    if user.role == User.Role.ADMIN:
        return redirect("admin_dashboard")

    elif user.role == User.Role.GURU:
        return redirect("guru_dashboard")

    elif user.role == User.Role.SISWA:
        return redirect("siswa_dashboard")

    return redirect("login")


@login_required
def admin_dashboard(request):

    if request.user.role != User.Role.ADMIN:
        return redirect_by_role(request.user)

    return render(
        request,
        "accounts/admin_dashboard.html"
    )


@login_required
def guru_dashboard(request):

    if request.user.role != User.Role.GURU:
        return redirect_by_role(request.user)

    return render(
        request,
        "accounts/guru_dashboard.html"
    )


@login_required
def siswa_dashboard(request):

    if request.user.role != User.Role.SISWA:
        return redirect_by_role(request.user)

    return render(
        request,
        "accounts/siswa_dashboard.html"
    )