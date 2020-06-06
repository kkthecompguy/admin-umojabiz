from django.urls import path
from .views import advert_create_view, advert_delete_view, advert_list_view, advert_update_view, advert_current_view

app_name = 'adverts'
urlpatterns = [
  path('', advert_list_view, name='advert-list'),
  path('current/', advert_current_view, name='current'),
  path('create/', advert_create_view, name='advert-create'),
  path('<str:pk>/update/', advert_update_view, name='advert-update'),
  path('<str:pk>/delete/', advert_delete_view, name='advert-delete'),
]