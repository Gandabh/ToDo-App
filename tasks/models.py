from django.db import models
from django.urls import reverse

# Create your models here.

class Task(models.Model):
    
    title=models.CharField('title', max_length=255)
    complete= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})
