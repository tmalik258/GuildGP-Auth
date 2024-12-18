from django.urls import path
from rest_framework import routers

from .viewsets import LoginViewSet, RefreshViewSet, RegisterViewSet, UserViewSet


router = routers.SimpleRouter()

# ##################################################################### #
# ############################## USER  ################################ #
# ##################################################################### #
router.register(r"users", UserViewSet, basename="user")


# ##################################################################### #
# ############################## AUTH  ################################ #
# ##################################################################### #
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")


urlpatterns = [
    *router.urls,
]
