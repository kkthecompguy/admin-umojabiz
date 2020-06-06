from django.db import models

# Create your models here.
class Applicant(models.Model):
  job_id = models.IntegerField()
  applicant_name = models.CharField(max_length=100)
  applicant_email = models.EmailField()
  cv = models.CharField(max_length=100)
  status = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.applicant_name


class AvailableJob(models.Model):
  user_id = models.IntegerField()
  job_id = models.IntegerField()
  title = models.TextField()
  description = models.TextField()
  salary = models.CharField(max_length=50, null=True, blank=True)
  experience = models.CharField(max_length=10,null=True, blank=True)
  status = models.IntegerField()
  location = models.CharField(max_length=100)
  education = models.CharField(max_length=100)
  availability = models.CharField(max_length=100)
  deadline = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title


class BussinessService(models.Model):
  bussiness_id = models.IntegerField()
  service_id = models.IntegerField()

  def __str__(self):
    return str(self.bussiness_id)


class Bussiness(models.Model):
  user_id = models.IntegerField()
  industry_id = models.IntegerField()
  location = models.CharField(max_length=100)
  business_name = models.CharField(max_length=200)
  description = models.TextField()
  logo = models.CharField(max_length=100, null=True, blank=True)
  phone = models.CharField(max_length=20)
  email = models.EmailField()
  website = models.CharField(max_length=100)
  address_latitude = models.CharField(max_length=100)
  address_longitude = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.business_name


class Industry(models.Model):
  industry_name = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.industry_name


class JobAlert(models.Model):
  email = models.EmailField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.email


class JobType(models.Model):
  job_name = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.job_name


class Keyword(models.Model):
  keyword_name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.keyword_name


class Location(models.Model):
  location = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.location


class Service(models.Model):
  service_name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.service_name


class Subscribe(models.Model):
  email = models.EmailField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.email


class Client(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  email_verified_at = models.CharField(max_length= 200, blank=True, null=True)
  password = models.CharField(max_length=200)
  remember_token = models.CharField(max_length=100, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name