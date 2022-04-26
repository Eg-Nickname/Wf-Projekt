from django.contrib import admin
from django.urls import path, include

from account.views import (
    registration_viev,
    logout_viev,
    login_viev,
    account_viev,
    change_password,
)
from obecnosc.views import (
    obecnosc_view,
    dziennik_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('obecnosc/', obecnosc_view, name="obecnosc_view"),
    path('dziennik/', dziennik_view, name="dziennik_view"),
    path('register/', registration_viev, name="register"),
    path('logout/', logout_viev, name="logout"),
    path('login/', login_viev, name="login"),
    path('account/', account_viev, name="account"),
    path('account/change_password', change_password, name="change_password"),
]
