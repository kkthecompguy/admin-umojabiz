from django.urls import path
from .views import home_view, agents_view, reports_view, tickets_view, business_update_view, business_delete_view, login_view, logout_view

app_name = 'core'
urlpatterns = [
  path('', home_view, name="index"),
  path('login/', login_view, name='login'),
  path('logout/', logout_view, name='logout'),
  path('agents/', agents_view, name="agents"),
  path('reports/', reports_view, name="reports"),
  path('tickets/', tickets_view, name="tickets"),
  path('business/<str:pk>/update/', business_update_view, name='business-update'),
  path('business/<str:pk>/delete/', business_delete_view, name='business-delete'),
]