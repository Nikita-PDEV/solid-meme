# news/views.py  

from django.shortcuts import render, get_object_or_404, redirect  
from django.views.generic import ListView  
from .models import Post, Comment, Author, Category  
from django.contrib.auth.decorators import login_required  
from django.views import View  
from django.utils.decorators import method_decorator  
from django.views.generic import ListView  
from .censor import censor_filter 

# Представление для списка новостей  
class NewsListView(ListView):  
    model = Post  
    template_name = 'news/news_list.html'   
    context_object_name = 'posts'  

class PostList(ListView):  
    model = Post  
    template_name = 'news/post_list.html'  
    context_object_name = 'posts'  
    
# Представление для детального просмотра поста  
class PostDetail(View):  
    def get(self, request, post_id):  
        post = get_object_or_404(Post, id=post_id)  
        comments = post.comment_set.all()  
        return render(request, 'news/post_detail.html', {'post': post, 'comments': comments})  


# Представление для создания поста  
@method_decorator(login_required, name='dispatch')  
class PostCreate(View):  
    def get(self, request):  
        return render(request, 'news/post_form.html')  

    def post(self, request):  
        title = request.POST.get('title')  
        content = censor_filter(request.POST.get('content'))  
        post_type = request.POST.get('post_type')  
        author = request.user.author  

        post = Post.objects.create(author=author, title=title, content=content, post_type=post_type)  
        return redirect('post_detail', post_id=post.id)  


# Представление для редактирования поста  
@method_decorator(login_required, name='dispatch')  
class PostEdit(View):  
    def get(self, request, post_id):  
        post = get_object_or_404(Post, id=post_id)  
        return render(request, 'news/post_form.html', {'post': post})  

    def post(self, request, post_id):  
        post = get_object_or_404(Post, id=post_id)  
        post.title = request.POST.get('title')  
        post.content = censor_filter(request.POST.get('content'))  # Используем censor_filter  
        post.save()  
        return redirect('post_detail', post_id=post.id)  


# Представление для удаления поста  
@method_decorator(login_required, name='dispatch')  
class PostDelete(View):  
    def get(self, request, post_id):  
        post = get_object_or_404(Post, id=post_id)  
        return render(request, 'news/confirm_delete.html', {'post': post})  

    def post(self, request, post_id):  
        post = get_object_or_404(Post, id=post_id)  
        post.delete()  
        return redirect('news_list')