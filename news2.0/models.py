from django.db import models  
from django.contrib.auth.models import User  
from django.utils import timezone  

class Category(models.Model):  
    name = models.CharField(max_length=100)  

class Subscription(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    subscribed_on = models.DateTimeField(auto_now_add=True)  

    class Meta:  
        unique_together = ('user', 'category')  
class Author(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    rating = models.IntegerField(default=0)  

    def update_rating(self):  
        post_rating = sum(post.rating * 3 for post in self.post_set.all())  
        comment_rating = sum(comment.rating for comment in self.user.comment_set.all())  
        author_comment_rating = sum(comment.rating for post in self.post_set.all() for comment in post.comment_set.all())  
        self.rating = post_rating + comment_rating + author_comment_rating  
        self.save()  

class Category(models.Model):  
    name = models.CharField(max_length=100, unique=True)  

class Post(models.Model):  
    ARTICLE = 'AR'  
    NEWS = 'NW'  
    POST_TYPE_CHOICES = [  
        (ARTICLE, 'Статья'),  
        (NEWS, 'Новость'),  
    ]  

    author = models.ForeignKey(Author, on_delete=models.CASCADE)  
    post_type = models.CharField(max_length=2, choices=POST_TYPE_CHOICES)  
    created_at = models.DateTimeField(auto_now_add=True)  
    categories = models.ManyToManyField('Category', through='PostCategory')  
    title = models.CharField(max_length=200)  
    text = models.TextField()  
    rating = models.IntegerField(default=0)  

    def like(self):  
        self.rating += 1  
        self.save()  

    def dislike(self):  
        self.rating -= 1  
        self.save()  

    def preview(self):  
        return self.text[:124] + '...' if len(self.text) > 124 else self.text  

class PostCategory(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  

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