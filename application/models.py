from django.db import models

# Create your models here.

class ApplicationModel(models.Model):
	main_wow_character = models.CharField(max_length=50)
	created_on = models.DateTimeField(auto_now_add=True)
	dnd_experience = models.TextField()
	describe_your_dnd_character = models.TextField()
	player_gender = models.CharField(max_length=50)
	describe_player_personality = models.TextField()
	guild_leadership = models.BooleanField()

	class _meta:
		ordering = ['-created_on']
		abstract = False
		swapped = False
		app_label = "application"
		get_latest_by = ['-created_on']

	def __str__(self):
		return self.main_wow_character
