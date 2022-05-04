from django import forms
import random
thousand_list = range(0,1000)

class ApplicationForm(forms.Form):
	tie_breaker = forms.IntegerField(random.choice(thousand_list))
	main_character = forms.CharField(max_length=200, unique=False)
	slug = forms.SlugField(max_length=200, unique=True)
	created_on = forms.DateTimeField(auto_now_add=True)
	dnd_experience = forms.CharField(unique=False)
	describe_your_character = forms.Charfield(unique=False)
	player_gender = forms.Charfield(unique=False)
	guild_leadership = forms.Charfield(unique=False)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.main_character
