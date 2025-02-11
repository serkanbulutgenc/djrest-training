from django.urls import path

from apps.account.api.views import signin, signout

urlpatterns = [
    path("signin/", signin, name="signin"),
    path("signout/", signout, name="signout"),
]
