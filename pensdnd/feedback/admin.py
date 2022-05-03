from django.contrib import admin
from .models import FeedbackForm

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('subject', 'slug', 'author', 'created_on')
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(FeedbackForm, FeedbackAdmin)
