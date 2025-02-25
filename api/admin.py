from django.contrib import admin
from .models import Individual

from api.models import CustomUser
# Register your models here.

@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ["name", "national_id", "age", "phone_number", "address"]
    search_fields = ["name", "national_id", "phone_number"]
    list_filter = ["age"]
    list_per_page = 30
    
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "phone_number", "api_key",
                    "is_premium", "credits", "last_request_time"]
    search_fields = ["username", "phone_number"]
    list_filter = ["is_premium"]
    list_per_page = 30