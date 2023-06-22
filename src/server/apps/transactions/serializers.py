from rest_framework import serializers

from .models import PaymentReceipt


class PaymentReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReceipt
        exclude = ("user",)
        read_only_fields = ("date",)

    def create(self, validated_data):
        validated_data.update({"user_id": self.context["request"].user.id})
        return super().create(validated_data)
