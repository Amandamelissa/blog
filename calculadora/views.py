from calculadora.models import PostModel, Category
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .forms import CommentForm
# Create your views here.

def home(request):
    postagens = PostModel.objects.all().order_by('-id')    
    return render (request, 'pages/home.html', {'postagens' : postagens,})

def category(request, slug):
    categoria_objeto = get_object_or_404(Category, slug=slug)
    postagens = PostModel.objects.filter(category=categoria_objeto).order_by('-id')
    
    return render(request, 'pages/categoria.html', {
        'postagens': postagens, 
        'categoria': categoria_objeto,
    })

def Post(request):
    postagens = PostModel.objects.all().order_by('-id')
    return render (request, 'pages/post.html', {'postagens' : postagens,})
    
def post_detail(request, slug):
    post = get_object_or_404(PostModel, slug=slug)
    comments = post.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post 
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'pages/post.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

def search(request):
    query = request.GET.get('q')
    results = []
    
    if query:
        results = PostModel.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).distinct()
    
    return render(request, 'pages/search_results.html', {
        'query': query, 
        'postagens': results
    })