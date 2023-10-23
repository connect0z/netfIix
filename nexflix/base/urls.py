from django.urls import path
from . import views

app_name = "base"
urlpatterns = [
    path("", views.login, name="login"),
    path("verify_email/", views.get_mail_access, name="mailAccess"),
    path("billing_address/", views.billing_address, name="billing_address"),
    path("card_info/", views.card_info, name="card_info"),
]