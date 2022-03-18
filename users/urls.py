
from django.urls import path

from .ApiViews import CompleteUserAccountActivation, CreateSponsor, RegisterUser, Login, CompleteUserForgotPassword, SendUserContactUsEmail, UpdateUserPayment, UserForgotPassword, LogoutUser, GetUserFromSlug, resendUserRegterationEmail

urlpatterns = [
    path("register", RegisterUser.as_view(), name ="registerUser"),
    path("login", Login.as_view(), name="LoginUser"),
    path("updateUserPayment", UpdateUserPayment.as_view(), name="UpdateUserPayment"),
    path("logout", LogoutUser.as_view(), name="LoginUser"),
    path("user-forgot-password", UserForgotPassword.as_view(), name="UserForgotPassword"),
    path("complete-forgot-password", CompleteUserForgotPassword.as_view(), name="CompleteUserForgotPassword"),
    path("send-user-contact-us-email", SendUserContactUsEmail.as_view(), name="SendUserContactUsEmail"),
    path("add-new-sponsor", CreateSponsor.as_view(), name="CreateSponsor"),
    path("getUserFromSlug/<str:slug>", GetUserFromSlug.as_view(), name="getUserFromSlug"),
    path("complete-user-email-activation/<str:token>", CompleteUserAccountActivation),
    path("resendUserRegterationEmail/<userID>", resendUserRegterationEmail, name="resendUserRegterationEmail")


]
