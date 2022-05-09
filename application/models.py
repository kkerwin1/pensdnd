from django.db import models
import random
thousand_list = range(0,1000)

# Create your models here.

class ApplicationModel(models.Model):
	i = random.choice(thousand_list)
	tie_breaker = models.IntegerField(i)
	main_wow_character = models.CharField(max_length=50)
	slug = models.SlugField()
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
