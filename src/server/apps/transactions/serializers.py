from rest_framework import serializers

from .models import PaymentCategory, PaymentReceipt


class PaymentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCategory
        fields = "__all__"


class PaymentReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReceipt
        exclude = ("user",)
        read_only_fields = ("date",)

    def create(self, validated_data):
        print(validated_data)
        validated_data.update({"user_id": self.context["request"].user.id})
        return super().create(validated_data)
