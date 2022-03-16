from django.urls import path

from companies.ApiViews import RegisterCompany, LoginCompany, UpdateCompanyPlan, GetCompanyFromSlug


urlpatterns = [
    path("register", RegisterCompany.as_view(), name="RegisterCompany" ),
    path("login", LoginCompany.as_view(), name="RegisterCompany" ),
    path("updatePlan", UpdateCompanyPlan.as_view(), name="Update Company Plan"),
    path("getCompanyBySlug/<slug>", GetCompanyFromSlug.as_view(), name="GetCompanyBySlug"),

]
