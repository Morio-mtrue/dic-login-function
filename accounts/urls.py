from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('detail/', views.detail, name='detail'),
    path('edit/', views.edit, name='edit'),
    path('password/', views.password_change, name='password_change'),
    path('delete/', views.delete, name='delete'),
]
