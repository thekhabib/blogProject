from django.contrib.auth.views import LoginView
from django.urls import path
from .views import SignupView, LogoutCustomView

urlpatterns = [
    path('register/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutCustomView.as_view(), name='logout'),
]
