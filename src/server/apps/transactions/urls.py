from rest_framework.routers import SimpleRouter

from .views import PaymentReceiptViewSet

router = SimpleRouter()

router.register("payment", PaymentReceiptViewSet, basename="payment")

urlpatterns = router.urls
