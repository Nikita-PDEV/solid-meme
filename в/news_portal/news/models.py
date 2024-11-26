from django.db import models  
from django.contrib.auth.models import User  
from django.core.exceptions import ValidationError  


def censor_filter(text):  
    # Этот метод проверяет и цензурирует текст  
    bad_words = ['badword1', 'badword2']    
    for word in bad_words:  
        text = text.replace(word, '*' * len(word))  
    return text  


class Author(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    rating = models.IntegerField(default=0)  

    def update_rating(self):  
        post_ratings = sum(post.rating * 3 for post in self.post_set.all())  
        comment_ratings = sum(comment.rating for comment in Comment.objects.filter(user=self.user))  
        comment_ratings_to_posts = sum(comment.rating for post in self.post_set.all() for comment in post.comment_set.all())  
        self.rating = post_ratings + comment_ratings + comment_ratings_to_posts  
        self.save()  

    def __str__(self):  
        return self.user.username  


class Category(models.Model):  
    name = models.CharField(max_length=100, unique=True)  

    def __str__(self):  
        return self.name  


class Post(models.Model):  
    ARTICLE = 'AR'  
    NEWS = 'NW'  
    POST_TYPE_CHOICES = [  
        (ARTICLE, 'Article'),  
        (NEWS, 'News'),  
    ]  

    author = models.ForeignKey(Author, on_delete=models.CASCADE)  
    post_type = models.CharField(max_length=2, choices=POST_TYPE_CHOICES)  
    created_at = models.DateTimeField(auto_now_add=True)  
    categories = models.ManyToManyField(Category, through='PostCategory')  
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    rating = models.IntegerField(default=0)  

    def like(self):  
        self.rating += 1  
        self.save()  

    def dislike(self):  
        self.rating -= 1  
        self.save()  

    def preview(self):  
        return self.content[:124] + '...' if len(self.content) > 124 else self.content  

    def __str__(self):  
        return self.title  # Добавлен метод для удобства отображения  


class PostCategory(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  

    def __str__(self):  
        return f"{self.post.title} in {self.category.name}"  # Удобное отображение  


class Comment(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    text = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    rating = models.IntegerField(default=0)  

    def like(self):  
        self.rating += 1  
        self.save()  

    def dislike(self):  
        self.rating -= 1  
        self.save()  

    def __str__(self):  
        return f"Comment by {self.user.username} on {self.post.title}"  # Удобное отображение