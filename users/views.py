from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm, UserChangeForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, message=f"{username} Succesfully signed up.")
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {"title": "Home-Authorization", "form": form}
    return render(request, "users/login.html", context)


def registration(request):

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(
                request, message=f"{user.username} Succesfully registered."
            )
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {"title": "Home-Register", "form": form}
    return render(request, "users/registration.html", context)


@login_required
def profile(request):

    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, message="Succesfully modified profile")
            return HttpResponseRedirect(reverse("user:profle"))
    else:
        form = ProfileForm(instance=request.user)

    context = {"title": "Home-Account"}
    return render(request, "users/profile.html", context)


def logout(request):
    messages.success(request, message=f"{request.user.username} Succesfully logout.")
    auth.logout(request)

    return redirect(reverse("main:index"))
