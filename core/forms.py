from django import forms
from .models import Bussiness


class BusinessForm(forms.ModelForm):

  class Meta:
    model = Bussiness
    fields = '__all__'