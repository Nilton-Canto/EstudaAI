from django.urls import path
from .import views

urlpatterns = [
    path(
        'Accounts/signup',
        views.AccountCreateView.as_view(),
        name='signup'
    )
]