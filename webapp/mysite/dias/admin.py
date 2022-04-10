from django.contrib import admin

from .models import Company, Complaint
# Register your models here.
admin.site.register(Company)
admin.site.register(Complaint)
