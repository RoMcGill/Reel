from django.contrib import admin
from userauthentication.models import Profile

# admin.site.register(Profile)
# Register your models here.



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'created')