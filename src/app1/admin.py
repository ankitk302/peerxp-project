from django.contrib import admin
from .models import member
# Register your models here.
@admin.register(member)
class memberadmin(admin.ModelAdmin):

    list_display =('id','Name','Category', 'Amount','created_by')