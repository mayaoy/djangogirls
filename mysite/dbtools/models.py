from django.db import models

# Create your models here.
class Job(models.Model):
	company_name = models.CharField(max_length=100)
	job_title = models.CharField(max_length=100)
	depiction = models.TextField(blank=True)
	#photo = models.URLField(blank=True)
	start_at = models.DateField()
	end_at = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.company_name
