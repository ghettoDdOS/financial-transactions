from rest_framework.routers import SimpleRouter

from .views import PaymentCategoryViewSet, PaymentReceiptViewSet

router = SimpleRouter()

router.register("payment", PaymentReceiptViewSet, basename="payment")
router.register("category", PaymentCategoryViewSet, basename="category")

urlpatterns = router.urls
