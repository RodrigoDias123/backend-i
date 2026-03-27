from django.db import models
from django.contrib.auth import get_user_model


class Meeting(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    sumary = models.TextField()

    def __str__(self):
        return f"Meeting: {self.title}, {self.date}"

    class Meta:
        ordering = ["-date"]

