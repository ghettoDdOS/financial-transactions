from rest_framework import mixins, viewsets, parsers, renderers

from .models import PaymentReceipt
from .serializers import PaymentReceiptSerializer


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
