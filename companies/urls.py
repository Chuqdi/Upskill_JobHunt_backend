from django.urls import path

from companies.ApiViews import RegisterCompany, LoginCompany, UpdateCompanyPlan, GetCompanyFromSlug, UpdateProfile


urlpatterns = [
    path("register", RegisterCompany.as_view(), name="RegisterCompany" ),
    path("login", LoginCompany.as_view(), name="RegisterCompany" ),
    path("updatePlan", UpdateCompanyPlan.as_view(), name="Update Company Plan"),
    path("updateProfile/<companyID>", UpdateProfile.as_view(), name="UpdateProfile"),
    path("getCompanyBySlug/<slug>", GetCompanyFromSlug.as_view(), name="GetCompanyBySlug"),

]
