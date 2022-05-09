from django import forms

class FeedbackForm(forms.Form):
	subject = forms.CharField(max_length=200, label="Subject")
	slug = forms.SlugField(max_length=200)
	author = forms.CharField(empty_value="Anonymous", required=False, max_length=50, label="Author, defaults to anonymous")
	content = forms.CharField(label="Write your feedback here")
	created_on = forms.DateTimeField()

	class _meta:
		ordering=[-'created_on']
