from django.urls import path
from .views import ( 
  applicant_view, 
  available_job_view, 
  bussiness_service_view, 
  business_view, 
  indusries_view, 
  job_alerts_view, 
  job_types_view, 
  keyword_view, 
  location_view, 
  services_view, 
  subscribers_view, 
  clients_view,
  )  

urlpatterns = [
  path('applicant/', applicant_view, name='applicant'),
  path('available-jobs/', available_job_view, name='available-jobs'),
  path('bussiness-service/', bussiness_service_view, name='bussiness-service'),
  path('bussiness/', business_view, name='business'),
  path('industry/', indusries_view, name='industry'),
  path('job-alert/', job_alerts_view, name='job-alert'),
  path('job-type/', job_types_view, name='job-type'),
  path('keyword/', keyword_view, name='applicant'),
  path('location/', location_view, name='location'),
  path('service/', services_view, name='service'),
  path('subscribe/', subscribers_view, name='subscribe'),
  path('client/', clients_view, name='client'),
]