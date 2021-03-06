from django.contrib import admin
from .models import ApplicationModel
from .forms import ApplicationForm

# Register your models here.

@admin.register(ApplicationModel)
class ApplicationModelAdmin(admin.ModelAdmin):
	form = ApplicationForm
	list_display = ('main_wow_character', 'created_on', 'dnd_experience', 'describe_your_dnd_character', 'player_gender', 'describe_player_personality', 'guild_leadership')
	search_fields = ['main_wow_character']
