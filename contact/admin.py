from django.contrib import admin
from .models import Contact
# Register your models here.

# admin.site.register(Contact)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', 'subject')



