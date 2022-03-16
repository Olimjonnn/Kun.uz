from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'admin'),
        (2, 'client'),
    ), default=2)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Category(models.Model):
    name = models.CharField(max_length=217)
    def __str__(self):
        return self.name

class CategoryCity(models.Model):
    name = models.CharField(max_length=217)
    def __str__(self):
        return self.name


class ViderCategory(models.Model):
    name = models.CharField(max_length=217)
    def __str__(self):
        return self.name

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_city = models.ForeignKey(CategoryCity, on_delete=models.CASCADE, blank=True, null=True)
    category_video = models.ForeignKey(ViderCategory, on_delete=models.CASCADE, blank=True, null=True)    
    img1 = models.ImageField(upload_to="News/")
    img2 = models.ImageField(upload_to="News/", blank=True, null=True)
    img3 = models.ImageField(upload_to="News/", blank=True, null=True)
    video_link = models.CharField(max_length=300, blank=True, null=True)
    title1 = models.CharField(max_length=300)
    title2 = models.CharField(max_length=300, blank=True, null=True)
    title3 = models.CharField(max_length=300, blank=True, null=True)
    text1 = models.TextField()
    text2 = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField(default=True)
