from django.contrib import admin
from .forms import FeedbackForm

# Register your models here.

@admin.register(FeedbackForm)
class FeedbackAdmin(admin.ModelAdmin):
	form = FeedbackForm
	list_display = ['subject', 'slug', 'author', 'created_on', 'content']
	search_fields = ['subject', 'content']
	prepopulated_fields = {'slug': ('subject',)}
