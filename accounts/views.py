from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import LoginForm, SignUpForm, UserEditForm, UserPasswordChangeForm


class UserLoginView(LoginView):
    """Login page. Sends the user to the task list on success."""

    form_class = LoginForm
    template_name = 'accounts/login.html'


def signup(request):
    """Account registration, then straight into the task list."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks:index')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def user_logout(request):
    """Log out and return to the login page."""
    logout(request)
    return redirect('accounts:login')


@login_required
def detail(request):
    """Account details for the logged in user."""
    return render(request, 'accounts/detail.html', {'user_data': request.user})


@login_required
def edit(request):
    """Edit username, email and age."""
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'accounts/edit.html', {'form': form})


@login_required
def password_change(request):
    """Change the password, keeping the session signed in."""
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Changing the password rotates the session hash, so refresh it
            # to avoid logging the user straight back out.
            update_session_auth_hash(request, user)
            return redirect('accounts:detail')
    else:
        form = UserPasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {'form': form})


@login_required
def delete(request):
    """Close the account."""
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('accounts:login')
    return render(request, 'accounts/delete.html', {'user_data': request.user})
