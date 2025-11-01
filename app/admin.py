from django.contrib import admin
from app.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_filter = ('cost',)
    list_display = ('title',)
    search_fields = ('title',)
# admin.site.register(Item, ItemAdmin)
