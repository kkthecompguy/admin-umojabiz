import csv
import io
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from .models import Job
from core.models import Applicant, AvailableJob, Bussiness


@login_required(login_url='core:login')
def job_view(request):
  jobs = Job.objects.all()
  context = {
    'object_list': jobs,
    'jobs': 'Jobs',
    'updated_at': datetime.now()
  }
  return render(request, 'jobs/index.html', context)


@login_required(login_url='core:login')
def job_applicants_view(request):
  applicants = Applicant.objects.all()
  context = {
    'object_list': applicants,
    'applicants': 'Applicants',
    'updated_at': datetime.now()
  }
  return render(request, 'jobs/applicants.html', context)


@login_required(login_url='core:login')
def posted_job_view(request):
  posted_jobs = AvailableJob.objects.all()
  context = {
    'object_list': posted_jobs,
    'posted': 'Posted jobs',
    'updated_at': datetime.now()
  }
  return render(request, 'jobs/posted-jobs.html', context)


@login_required(login_url='core:login')
def bussiness_list_view(request):
  business = Bussiness.objects.all()
  context = {
    'object_list': business,
    'business': 'Business',
    'updated_at': datetime.now()
  }
  return render(request, 'jobs/business.html', context)


@login_required(login_url='core:login')
@permission_required('admin.can_add_log_entry')
def job_upload_view(request):
  if request.method == "POST":
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
      messages.error(request, "The file is not a csv file")
    
    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = Job.objects.get_or_create(
        amount=col[0],
        category_or_job_function=col[1],
        company=col[2],
        description=col[3],
        featured=col[4],
        full_time_or_part_time=col[5],
        job_type=col[6],
        location=col[7],
        working_hours=col[8]
      )
  return render(request, 'jobs/upload.html', {})