from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("registration", views.registration, name="registration"),
    path("2FA_login", views.FA2_login, name="2FA_login"),
    path("2FA_registration", views.FA2_registartion, name="2FA_registration"),
    path("complete_registration", views.complete_registration, name="complete_registration"),
    path("GIS", views.gis, name="gis")
]