from django.db import models


class Meeting(models.Model):
	title = models.CharField(max_length=200)
	scheduled_at = models.DateTimeField()

	def __str__(self) -> str:
		return self.title
