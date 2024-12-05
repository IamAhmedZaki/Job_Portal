from django.urls import path

from .views import SignupView,LoginView, logout_view,ChangePasswordAPI,PasswordResetRequestView,PasswordResetView
# from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("signup/", SignupView.as_view() ),
    path("login/", LoginView.as_view()),
    path("logout/", logout_view),
    path("change-password/",ChangePasswordAPI.as_view()),
    path('request-reset-password/', PasswordResetRequestView.as_view(), name='request-reset-password'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]