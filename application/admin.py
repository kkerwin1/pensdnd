from django.contrib import admin
from .forms import ApplicationForm

# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
	form = ApplicationForm
	list_display = ('main_character', 'slug', 'created_on', 'tie_breaker', 'dnd_experience', 'describe_your_character', 'player_gender', 'guild_leadership')
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(ApplicationForm, ApplicationAdmin)
