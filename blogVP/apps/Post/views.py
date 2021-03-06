from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, DisLike, Comment
from .forms import PostForm, CommentForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q


class PostListView(ListView):
    model = Post
    ordering = ['-publish_date']
    template_name='posts/post_list.html'
    context_object_name = 'posts'

def Busqueda(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.all()
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) | 
            Q(content__icontains = queryset) |
            Q(content__icontains = queryset)
        ).distinct()
        ctx = {}
        ctx['posts'] = posts
        return render(request, 'posts/post_busqueda.html', ctx)
    else:
        ctx = {}
        ctx['posts'] = posts
        return render(request, 'posts/post_busqueda.html', ctx)

def Filtrar(request):
    queryset = request.GET.get("filtrar")
    author = Post.objects.all()
    if queryset:
        author = Post.objects.filter(
            Q(author_id = queryset)
        )
        ctx = {}
        ctx['author'] = author
        return render(request, 'posts/post_ods.html', ctx)
    else:
        author = Post.objects.exclude(author_id = 1)
        ctx = {}
        ctx['author'] = author
        return render(request, 'posts/post_posts.html', ctx)

class PostDetailView(DetailView):
    model = Post
    template_name='posts/post_detail.html'

    def post(self, *args, **kwargs):
        liked = False
        
        context = super().get_context_data(**kwargs)
        print("\n\n\n",context,"\n\n\n")
        things = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = things.get_like_count()

        if things.like.filter(id = self.request.user.id).exist():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked

        return context


class PostCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/post_comment.html'
    success_url = '/'
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        x = form.save(commit = False)
        x.post_id = self.kwargs['pk']
        x.user = self.request.user
        x.save()

        return HttpResponseRedirect(reverse('Post:detail', args=[str(x.post_id)]))


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'posts/post_form.html'
    success_url = '/'
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.instance.thumbnail.name:
            ext = form.instance.thumbnail.name.split(".")[-1]
            form.instance.thumbnail.name = form.instance.title + '.' + ext

        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'update'
        })
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = '/'


def like(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    print(post.like.filter(id = request.user.id).exists())

    if post.like.filter(id = request.user.id).exists():
        post.like.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('Post:detail', args = [str(pk)]))

