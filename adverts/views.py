from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Advert
from .forms import AdvertForm


# Create your views here.
@login_required(login_url='core:login')
def advert_list_view(request):
  adverts = Advert.objects.all()
  context = {
    'advert': 'Adverts',
    'object_list': adverts
  }
  return render(request, 'adverts/index.html', context)


@login_required(login_url='core:login')
def advert_current_view(request):
  adverts = Advert.objects.filter(status=True)
  context = {
    'advert': 'Adverts',
    'object_list': adverts
  }
  return render(request, 'adverts/index.html', context)


@login_required(login_url='core:login')
def advert_create_view(request):
  form = AdvertForm(request.POST or None, request.FILES or None)
  if request.method == "POST":
    if form.is_valid():
      form.save()
      return redirect('adverts:advert-list')
  context = {
    'advert': 'Create Advert',
    'form': form,
    'title': 'Create'
  }
  return render(request, 'adverts/create.html', context)


@login_required(login_url='core:login')
def advert_update_view(request, pk):
  advert = get_object_or_404(Advert, pk=pk)
  form = AdvertForm(request.POST or None, request.FILES or None, instance=advert)
  if request.method == "POST":
    if form.is_valid():
      form.save()
      return redirect('adverts:advert-list')
  context = {
    'advert': 'Update Advert',
    'form': form,
    'title': 'Update'
  }
  return render(request, 'adverts/create.html', context)


@login_required(login_url='core:login')
def advert_delete_view(request, pk):
  advert = get_object_or_404(Advert, pk=pk)
  advert.delete()
  return redirect('adverts:advert-list')