from django.db import models

# Create your models here.

class FeedbackModel(models.Model):
	subject = models.CharField(max_length=200)
	slug = models.SlugField()
	author = models.CharField(max_length=200)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	img = models.ImageField(upload_to = "images/")

	class Meta:
		ordering = ['-created_on']
		app_label = "feedback"

	class _meta:
		model_name = "FeedbackModel"
		abstract = False
		get_latest_by = ['-created_on']
