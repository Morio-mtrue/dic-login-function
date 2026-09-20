# dic-login-function

Session login series assignment - Login function implementation.

Built on the `loginTask` starter. A custom user inheriting `AbstractBaseUser`
was added, along with registration, login, logout, account details, editing,
password change and account deletion. The existing task CRUD still works.

## Custom user

`accounts/models.py` defines `CustomUser(AbstractBaseUser, PermissionsMixin)`
with `CustomUserManager`. Login uses the email address
(`USERNAME_FIELD = 'email'`).

| Column | Field class | Validation | Default |
| --- | --- | --- | --- |
| username | CharField | max 150 characters | - |
| email | EmailField | unique | - |
| age | PositiveIntegerField | - | 0 |
| is_superuser | BooleanField | - | False |
| is_staff | BooleanField | - | False |
| is_active | BooleanField | - | True |
| date_joined | DateTimeField | - | current time |

`AUTH_USER_MODEL = 'accounts.CustomUser'` is set in settings.

## Screens

| URL | Screen | Title |
| --- | --- | --- |
| `/accounts/signup/` | Account registration | Member Registration Page |
| `/accounts/login/` | Login | Login page |
| `/accounts/logout/` | Logout | redirects to Login |
| `/accounts/detail/` | Account details | Member Information Details Page |
| `/accounts/edit/` | Account edit | Member Information Edit Page |
| `/accounts/password/` | Password change | Password Change Page |
| `/accounts/delete/` | Account deletion | Unsubscribe Page |

Transitions: registering logs the user straight in and lands on the task list.
Logging in goes to the task list. Logging out returns to the login page.
Editing and password change return to the account details page. Withdrawing
deletes the account and returns to the login page. Task pages require a login,
so an anonymous visitor is redirected to `/accounts/login/`.

## Global navigation

| Logged out | Logged in |
| --- | --- |
| Member Registration, Login | Task list, Member Information, Log out |

## Verified

| Check | Result |
| --- | --- |
| Model fields | id, password, last_login, username, email, age, is_superuser, is_staff, is_active, date_joined |
| Anonymous hitting `/tasks/` | 302 to `/accounts/login/?next=/tasks/` |
| Registration | User created with age 28, is_active True, is_staff False, is_superuser False, date_joined set |
| Password storage | Hashed, `check_password` passes |
| Navigation | Correct links shown and hidden in both states |
| All seven screens | 200 with the specified titles |
| Task CRUD | create, detail, edit, delete all still work while logged in |
| Account edit | username, email and age updated |
| Password change | New password works, session stays signed in |
| Logout then login by email | Works, task list reachable again |
| Duplicate email | Rejected, only one user remains |
| Password confirmation mismatch | Rejected, no user created |
| Withdraw | User deleted, redirected to login, task pages locked again |

## A note on wording

Screen labels follow the English table in the assignment brief. The task
templates that shipped with the starter are in Japanese, and
`LANGUAGE_CODE = 'ja'` means Django's own validation messages also appear in
Japanese. If the screens are meant to be in Japanese to match, the strings are
all in `accounts/templates/accounts/`, `accounts/forms.py` and
`templates/base.html`.

## Run

```
python3 -m venv venv && source venv/bin/activate
pip install django
createdb login_task
python manage.py migrate
python manage.py runserver
```

Then open <http://localhost:8000/accounts/signup/>.
