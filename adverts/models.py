from django.db import models
from django.urls import reverse

# Create your models here.
class Advert(models.Model):
  title = models.CharField(max_length=100)
  banner = models.ImageField()
  status = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

  def get_update_url(self):
    return reverse('adverts:advert-update',  kwargs={
      'pk': self.pk
    })

  def get_delete_url(self):
    return reverse('adverts:advert-delete',kwargs={
      'pk': self.pk
    })