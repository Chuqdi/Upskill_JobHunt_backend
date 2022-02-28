
from django.urls import path
from .ApiViews import CompleteUserAccountActivation, RegisterUser, Login, CompleteUserForgotPassword, UserForgotPassword, LogoutUser

urlpatterns = [
    path("register", RegisterUser.as_view(), name ="registerUser"),
    path("login", Login.as_view(), name="LoginUser"),
    path("logout", LogoutUser.as_view(), name="LoginUser"),
    path("complete-user-email-activation/<str:token>", CompleteUserAccountActivation),
    path("user-forgot-password", UserForgotPassword.as_view(), name="UserForgotPassword"),
    path("complete-forgot-password", CompleteUserForgotPassword.as_view(), name="CompleteUserForgotPassword")
]
