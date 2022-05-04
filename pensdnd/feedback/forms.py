from django import forms

class FeedbackForm(forms.Form):
	subject = models.CharField(max_length=200, unique=False)
	slug = models.SlugField(max_length=200, unique=True)
	author = forms.CharField(empty_value="Anonymous", max_length=50)
	content = models.TextField(empty_value="Please enter your feedback here.")
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title
