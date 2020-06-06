from django.urls import path
from .views import job_upload_view, job_view, job_applicants_view, posted_job_view, bussiness_list_view

app_name = 'jobs'
urlpatterns = [
  path('', job_view, name='job-index'),
  path('applicants/', job_applicants_view, name='job-applicants'),
  path('posted/', posted_job_view, name='job-posted'),
  path('business/', bussiness_list_view, name='business'),
  path('upload/', job_upload_view, name='job-upload'),
]