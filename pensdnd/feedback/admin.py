from django.contrib import admin
from .forms import FeedbackForm
from api.admin_forms import AdminForm

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
	form = FeedbackForm
	list_display = ('subject', 'slug', 'author', 'created_on')
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(FeedbackForm, FeedbackAdmin)
