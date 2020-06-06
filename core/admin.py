from django.contrib import admin
from .models import ( 
  Applicant, 
  AvailableJob, 
  Bussiness, 
  BussinessService, 
  Client, 
  Industry, 
  JobAlert, 
  JobType, 
  Keyword, 
  Location, 
  Subscribe,
  Service
  )

# Register your models here.
admin.site.register(Applicant)
admin.site.register(AvailableJob)
admin.site.register(Bussiness)
admin.site.register(BussinessService)
admin.site.register(Client)
admin.site.register(Industry)
admin.site.register(JobAlert)
admin.site.register(JobType)
admin.site.register(Keyword)
admin.site.register(Location)
admin.site.register(Service)
admin.site.register(Subscribe)