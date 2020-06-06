from django.db import models
from django.urls import reverse

# Create your models here.
class Job(models.Model):
  amount = models.CharField(max_length=100)
  category_or_job_function = models.CharField(max_length=200)
  company = models.CharField(max_length=100)
  description = models.TextField()
  featured = models.CharField(max_length=5)
  full_time_or_part_time = models.CharField(max_length=50)
  job_type = models.CharField(max_length=200)
  location = models.CharField(max_length=100)
  working_hours = models.CharField(max_length=5)

  def __str__(self):
    return self.job_type

  def get_absolute_url(self):
    return reverse('jobs:job-detail', kwargs={
      'pk': self.pk
    })

  def get_update_url(self):
    return reverse('jobs:job-update', kwargs={
      'pk': self.pk
    })
  def get_delete_url(self):
    return reverse('jobs:job-delete', kwargs={
      'pk': self.pk
    })