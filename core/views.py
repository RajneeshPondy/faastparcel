from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from core.forms import SignUpForm


def home(request):
    return render(request, "home.html")


@login_required
def customer_page(request):
    return render(request, "home.html")


@login_required
def courier_page(request):
    return render(request, "home.html")


def sign_up(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            user = form.save(commit=False)
            user.username = email
            user.save()

            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/")

    return render(request, "sign_up.html", {"form": form})
