from django.contrib import admin
from .models import FeedbackModel

# Register your models here.

@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
	list_display = ['subject', 'slug', 'author', 'created_on', 'content', 'img']
	search_fields = ['subject', 'content']
	prepopulated_fields = {'slug': ('subject',)}
