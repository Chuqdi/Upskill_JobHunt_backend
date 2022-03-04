from django.urls import path

from companies.ApiViews import RegisterCompany, LoginCompany


urlpatterns = [
    path("create", RegisterCompany.as_view(), name="RegisterCompany" ),
    path("login", LoginCompany.as_view(), name="RegisterCompany" ),

]
