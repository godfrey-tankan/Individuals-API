from django.contrib import admin
from .models import Individual

# Register your models here.

@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ["name", "national_id", "age", "phone_number", "address"]
    search_fields = ["name", "national_id", "phone_number"]
    list_filter = ["age"]
    list_per_page = 10