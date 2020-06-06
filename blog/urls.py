from django.urls import path
from .views import home_view, post_detail_view, post_update_view, post_delete_view, post_create_view, post_list_view

app_name = 'blog'
urlpatterns = [
  path('', home_view, name='index'),
  path('post/create/', post_create_view, name='post-create'),
  path('post/list/', post_list_view, name='post-list'),
  path('post/<str:pk>/', post_detail_view, name='post-detail'),
  path('post/<str:pk>/update', post_update_view, name='post-update'),
  path('post/<str:pk>/delete', post_delete_view, name='post-delete'),
]