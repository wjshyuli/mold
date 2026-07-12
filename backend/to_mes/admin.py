from django.contrib import admin
from .models import Correspondence, Stock


@admin.register(Correspondence)
class CorrespondenceAdmin(admin.ModelAdmin):

    list_display = (
        "capsule",
        "specification",
        "clamp",
    )

    search_fields = (
        "capsule",
        "specification",
    )

    list_filter = (
        "clamp",
    )




@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass