from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Client, Applicant, AvailableJob, Service, Bussiness
from .forms import BusinessForm
from .decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def login_view(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      return redirect('core:index')
  return render(request, "core/login.html", {})


def logout_view(request):
  logout(request)
  return redirect('core:login')


@login_required(login_url='core:login')
def home_view(request):
  clients = Client.objects.all()
  applicant_count = Applicant.objects.all().count()
  available_job_count = AvailableJob.objects.all().count()
  service_count = Service.objects.all().count()
  businesses = Bussiness.objects.all()
  updated_at = datetime.today()

  context = {
    'dashboard': 'Dashboard',
    'businesses': businesses,
    'client_count': clients.count(),
    'applicant_count': applicant_count,
    'service_count': service_count,
    'available_job_count': available_job_count, 
    'updated_at': updated_at
    }
  return render(request, 'core/index.html', context)


@login_required(login_url='core:login')
def agents_view(request):
  clients = Client.objects.all()
  context = {
    'display': 'Clients',
    'clients': clients
    }
  return render(request, 'core/agents.html', context)


@login_required(login_url='core:login')
def reports_view(request):
  context = {'reports': 'Reports'}
  return render(request, 'core/reports.html', context)


@login_required(login_url='core:login')
def tickets_view(request):
  context = {'tickets': 'Tickets'}
  return render(request, 'core/tickets.html', context)


@login_required(login_url='core:login')
def business_update_view(request, pk):
  business = get_object_or_404(Bussiness, pk=pk)
  form = BusinessForm(request.POST or None, instance=business)
  if request.method == "POST":
    if form.is_valid():
      form.save()
      return redirect('core:index')
  context = {
    'form': form,
    'business': 'Business Update'
  }
  return render(request, 'core/update.html', context)


@login_required(login_url='core:login')
def business_delete_view(request, pk):
  business = get_object_or_404(Bussiness, pk=pk)
  business.delete()
  return redirect('core: index')
