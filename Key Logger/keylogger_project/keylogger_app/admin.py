from django.contrib import admin
from .models import KeyLog

@admin.register(KeyLog)
class KeyLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'keys')
    readonly_fields = ('timestamp', 'keys')