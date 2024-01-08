from django.contrib import admin

from service.models import RepairRequest


@admin.register(RepairRequest)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'user', 'engineer', 'solution', 'created_at', 'updated_at')
