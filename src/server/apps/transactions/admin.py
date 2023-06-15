from django.contrib import admin

from .models import PaymentReceipt


@admin.register(PaymentReceipt)
class PaymentReceiptAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "personal_acc",
        "bank_name",
        "bic",
        "corresp_acc",
    )
    list_filter = ("user",)
