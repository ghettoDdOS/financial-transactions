from django.contrib import admin

from .models import PaymentCategory, PaymentReceipt


@admin.register(PaymentReceipt)
class PaymentReceiptAdmin(admin.ModelAdmin):
    list_display = (
        "Name",
        "PersonalAcc",
        "BankName",
        "BIC",
        "CorrespAcc",
    )
    list_filter = ("user",)


@admin.register(PaymentCategory)
class PaymentCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
