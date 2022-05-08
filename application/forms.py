from django import forms
from django.db import models
import random
thousand_list = range(0,1000)

class ApplicationForm(forms.Form):
	i = random.choice(thousand_list)
	tie_breaker = models.IntegerField(i)
	main_character = forms.CharField(max_length=200)
	slug = forms.SlugField(max_length=200)
	created_on = forms.DateTimeField()
	dnd_experience = forms.CharField()
	describe_your_character = forms.CharField()
	player_gender = forms.CharField()
	describe_your_personality = forms.CharField()
	guild_leadership = forms.CharField()

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.main_character
