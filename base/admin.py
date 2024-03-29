from django.contrib import admin
from .models import ContactFormEntry


@admin.register(ContactFormEntry)
class ContactFormEntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'comments']
    search_fields = ['name', 'email']
