from django.db.models import Q
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Author, PostView, AnonymousView
from .forms import CommentForm, PostForm


def get_author(user):
  qs = Author.objects.filter(user=user)
  if qs.exists():
    return qs[0]
  return None
  

@login_required(login_url='core:login')
def home_view(request):
  queryset = Post.objects.filter(featured=True)
  context = {
    'blog': 'Blogs',
    'object_list': queryset
  }
  return render(request, 'blog/blog.html', context)


@login_required(login_url='core:login')
def post_list_view(request):
  queryset = Post.objects.filter()
  context = {
    'blog': 'All Post',
    'object_list': queryset
  }
  return render(request, 'blog/post-list.html', context)


@login_required(login_url='core:login')
def post_detail_view(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.user.is_authenticated:
    PostView.objects.get_or_create(
      user=request.user, 
      post=post
      )
  else:
    AnonymousView.objects.create(
      user=request.user, 
      post=post
      )
  form = CommentForm(request.POST or None)
  if request.method == "POST":
    if form.is_valid():
      form.instance.user = request.user
      form.instance.post = post
      form.save()
  context = {
    'post': post,
    'form': form,
    'blog': 'Create Post',
  }
  return render(request, 'blog/post-detail.html', context)


@login_required(login_url='core:login')
def post_create_view(request):
  form = PostForm(request.POST or None, request.FILES or None)
  author = get_author(request.user)
  if request.method == "POST":
    if form.is_valid():
      form.instance.author = author
      form.save()
      return redirect(reverse('blog:post-detail', kwargs={
        'pk': form.instance.id
      }))
  context = {
    'form': form,
    'blog': 'Create Post',
    'title': 'Create'
  }
  return render(request, 'blog/post-create.html', context)


@login_required(login_url='core:login')
def post_update_view(request, pk):
  post = get_object_or_404(Post, pk=pk)
  form = PostForm(request.POST or None, request.FILES or None, instance=post)
  author = get_author(request.user)
  if request.method == "POST":
    if form.is_valid():
      form.instance.author = author
      form.save()
      return redirect(reverse('blog:post-detail', kwargs={
        'pk': form.instance.id
      }))
  context = {
    'form': form,
    'blog': 'Create Post',
    'title': 'Update'
  }
  return render(request, 'blog/post-create.html', context)


@login_required(login_url='core:login')
def post_delete_view(request, pk):
  post = get_object_or_404(Post, pk=pk)
  post.delete()
  return redirect('blog:index')


def search_view(request):
  queryset = Post.objects.all()
  query = request.GET.get('q')
  if query:
    queryset = queryset.filter(
      Q(title__icontains=query) |
      Q(overview__icontains=query)
    ).distinct()
  context = {
    'queryset': queryset
  }
  return render(request, 'blog/search.html', context)