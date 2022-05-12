from django.contrib import admin
from .models import NameModel

# Register your models here.

@admin.register(NameModel)
class FeedbackAdmin(admin.ModelAdmin):
	list_display = ['name']
