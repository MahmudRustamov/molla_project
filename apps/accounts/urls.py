from django.urls import path
from apps.accounts.views import ConfirmEmailView, RegisterCreateView, LoginFormView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('confirmation/<uidb64>/<token>/', ConfirmEmailView.as_view(), name='confirmation'),
    # path('verification/', RegisterCreateView.as_view, name='register'),
    # path('resend/code/', RegisterCreateView.as_view, name='register'),
    # path('forget/password', RegisterCreateView.as_view, name='register'),
    # path('update/password', RegisterCreateView.as_view, name='register'),
]