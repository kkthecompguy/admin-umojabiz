import csv
import io
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from core.models import Applicant, AvailableJob, Bussiness, BussinessService, Client, Industry, JobAlert, JobType, Keyword, Location, Service, Subscribe


@permission_required('admin.can_add_log_entry')
def applicant_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = Applicant.objects.update_or_create(
        job_id=col[1],
        applicant_name=col[2],
        applicant_email=col[3],
        cv=col[4], 
        status=col[5],
        created_at=col[6],
        updated_at=col[7]
      )
  return render(request, 'core/upload.html', {})


@permission_required('admin.can_add_log_entry')
def available_job_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = AvailableJob.objects.update_or_create(
        user_id=col[1],
        job_id=col[2],
        title=col[3],
        description=col[4], 
        salary=col[5],
        experience=col[6],
        status=col[7],
        location=col[8],
        education=col[9],
        availability=col[10],
        deadline=col[11],
        created_at=col[12],
        updated_at=col[13]
      )
  return render(request, 'core/upload.html', {})
  

@permission_required('admin.can_add_log_entry')
def bussiness_service_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = BussinessService.objects.update_or_create(
        bussiness_id=col[1],
        service_id=col[2],
      )
  return render(request, 'core/upload.html', {})

  
@permission_required('admin.can_add_log_entry')
def business_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = Bussiness.objects.update_or_create(
        user_id=col[1],
        industry_id=col[2],
        location=col[3],
        business_name=col[4], 
        description=col[5],
        logo=col[6],
        phone=col[7],
        email=col[8],
        website=col[9],
        address_latitude=col[10],
        address_longitude=col[11],
        created_at=col[12],
        updated_at=col[13]
      )
  return render(request, 'core/upload.html', {})


@permission_required('admin.can_add_log_entry')
def indusries_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = Industry.objects.update_or_create(
        industry_name=col[1],
        created_at=col[2],
        updated_at=col[3],
      )
  return render(request, 'core/upload.html', {})


@permission_required('admin.can_add_log_entry')
def job_alerts_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = JobAlert.objects.update_or_create(
        email=col[1],
        created_at=col[2],
        updated_at=col[3]
      )
  return render(request, 'core/upload.html', {})


@permission_required('admin.can_add_log_entry')
def job_types_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = JobType.objects.update_or_create(
        job_name=col[1],
        created_at=col[2],
        updated_at=col[3],
      )
  return render(request, 'core/upload.html', {})


@permission_required('admin.can_add_log_entry')
def keyword_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = Keyword.objects.update_or_create(
        keyword_name=col[1],
        created_at=col[2],
        updated_at=col[3],
      )
  return render(request, 'core/upload.html', {})


@permission_required('admin.can_add_log_entry')
def location_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = Location.objects.update_or_create(
        location=col[1],
        created_at=col[2],
        updated_at=col[3],
      )
  return render(request, 'core/upload.html', {})


@permission_required('admin.can_add_log_entry')
def services_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = Service.objects.update_or_create(
        service_name=col[1],
        created_at=col[2],
        updated_at=col[3],
      )
  return render(request, 'core/upload.html', {})


@permission_required('admin.can_add_log_entry')
def subscribers_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = Subscribe.objects.update_or_create(
        email=col[1],
        created_at=col[2],
        updated_at=col[3],
      )
  return render(request, 'core/upload.html', {})



@permission_required('admin.can_add_log_entry')
def clients_view(request):
  if request.method == 'POST':
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
      message.error(request, 'The file type is a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=","):
      _, created = Client.objects.update_or_create(
        name=col[1],
        email=col[2],
        email_verified_at=col[3],
        password=col[4], 
        remember_token=col[5],
        created_at=col[6],
        updated_at=col[7]
      )
  return render(request, 'core/upload.html', {})