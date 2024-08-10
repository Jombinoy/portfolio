from django.contrib import admin
from .models import Contact  # Import your model

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')  # Adjust fields as needed
    search_fields = ('name', 'email', 'message')  # Add searchable fields


# admin.py
from django.contrib import admin
from .models import HireMe

@admin.register(HireMe)
class HireMeAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'salary_offering', 'bond', 'your_name', 'contact_no')
    search_fields = ('company_name', 'your_name')
    list_filter = ('bond',)


from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')
