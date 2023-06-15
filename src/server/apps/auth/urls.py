from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

from .views import UserViewset

router = SimpleRouter()

router.register("user", UserViewset, basename="user")

urlpatterns = [
    path(
        "token/",
        include(
            [
                path("", TokenObtainPairView.as_view(), name="token_obtain_pair"),
                path("verify/", TokenVerifyView.as_view(), name="token_verify"),
            ]
        ),
    ),
    *router.urls,
]
