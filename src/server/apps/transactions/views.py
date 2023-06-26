from rest_framework import mixins, parsers, renderers, viewsets

from .models import PaymentCategory, PaymentReceipt
from .serializers import PaymentCategorySerializer, PaymentReceiptSerializer


class PaymentReceiptViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PaymentReceiptSerializer
    queryset = PaymentReceipt.objects
    lookup_url_kwarg = "id"
    parser_classes = [parsers.JSONParser]
    renderer_classes = [renderers.JSONRenderer, renderers.BrowsableAPIRenderer]

    def get_queryset(self):
        return PaymentReceipt.objects.filter(user=self.request.user)


class PaymentCategoryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PaymentCategorySerializer
    queryset = PaymentCategory.objects.all()
    lookup_url_kwarg = "id"
    parser_classes = [parsers.JSONParser]
    renderer_classes = [renderers.JSONRenderer, renderers.BrowsableAPIRenderer]
