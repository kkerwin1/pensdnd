from django import forms

class FeedbackForm(forms.Form):
	subject = forms.CharField(max_length=200)
	slug = forms.SlugField(max_length=200)
	author = forms.CharField(empty_value="Anonymous", max_length=50)
	content = forms.CharField(empty_value="Please enter your feedback here.")
	created_on = forms.DateTimeField()

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title
