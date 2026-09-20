from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
)

from .models import CustomUser


class SignUpForm(UserCreationForm):
    """Account registration: username, email, age and a confirmed password."""

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age')
        labels = {
            'username': 'username',
            'email': 'Email address',
            'age': 'age',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password (for confirmation)'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input'


class LoginForm(AuthenticationForm):
    """Login with the email address and password."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email address'
        self.fields['password'].label = 'Password'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input'


class UserEditForm(forms.ModelForm):
    """Editing the account details, without touching the password."""

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age')
        labels = {
            'username': 'username',
            'email': 'Email address',
            'age': 'age',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input'


class UserPasswordChangeForm(PasswordChangeForm):
    """Password change, asking for the current password first."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = 'Original Password'
        self.fields['new_password1'].label = 'new password'
        self.fields['new_password2'].label = 'New password (for confirmation)'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input'
